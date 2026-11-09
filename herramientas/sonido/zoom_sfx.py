# Barrido de zoom zona<->mapa (Nuria). Síntesis procedural sin créditos: ruido filtrado con barrido en escala log.
import numpy as np, soundfile as sf, pyloudnorm as pyln, subprocess, sys
from scipy.signal import stft, istft
SR=48000
def barrido(seed, sube, dur=0.85, objetivo=-29.0):
    rng=np.random.default_rng(seed)
    n=int(SR*dur); t=np.arange(n)/SR
    out=[]
    f0,f1=(260,2600) if sube else (2600,260)
    f0*=rng.uniform(.85,1.15); f1*=rng.uniform(.85,1.15)
    curva=rng.uniform(1.4,2.2)
    for ch in range(2):
        x=rng.standard_normal(n+SR//5)
        f,tt,Z=stft(x,SR,nperseg=1024,noverlap=768)
        u=np.clip(tt/dur,0,1)
        k=u**curva if sube else 1-(1-u)**curva
        fc=np.exp(np.log(f0)+(np.log(f1)-np.log(f0))*k)
        lf=np.log(np.maximum(f,1))[:,None]
        bw=rng.uniform(.55,.75)
        g=np.exp(-0.5*((lf-np.log(fc)[None,:])/bw)**2)
        _,y=istft(Z*g,SR,nperseg=1024,noverlap=768); y=y[:n]
        out.append(y)
    y=np.stack(out,1)
    # envolvente: ataque suave, cresta hacia el 55 %, cola
    a=np.clip(t/(0.18*dur),0,1)**1.5; r=np.clip((dur-t)/(0.45*dur),0,1)**2
    env=np.minimum(a,r)*(0.6+0.4*np.sin(np.pi*np.clip(t/dur,0,1)))
    y*=env[:,None]
    # golpe grave al llegar a la zona (entrar) o «chasquido» de radio al llegar al mapa (salir)
    if not sube:
        tc=0.70*dur; th=np.clip(t-tc,0,None); thump=np.sin(2*np.pi*(55+25*np.exp(-th*30))*th)*np.exp(-th*14)*(t>=tc)
        y+=0.35*thump[:,None]*np.max(np.abs(y))
    else:
        tc=0.74*dur; m=(t>=tc)&(t<tc+0.06); c=rng.standard_normal(n)*m*np.exp(-np.clip(t-tc,0,None)*60)
        from scipy.signal import butter,sosfilt
        c=sosfilt(butter(4,[1800,4200],'bandpass',fs=SR,output='sos'),c)
        y+=0.5*c[:,None]*np.max(np.abs(y))/max(1e-9,np.max(np.abs(c)))
    # fundidos de 5 ms
    fd=int(.005*SR); w=np.linspace(0,1,fd); y[:fd]*=w[:,None]; y[-fd:]*=w[::-1,None]
    meter=pyln.Meter(SR,block_size=0.2)
    l=meter.integrated_loudness(y); y*=10**((objetivo-l)/20)
    pk=20*np.log10(np.max(np.abs(y)))
    if pk>-1.5: y*=10**((-1.5-pk)/20)
    return y, meter.integrated_loudness(y), 20*np.log10(np.max(np.abs(y)))
for sube,nom in ((True,'sfx_zoom_salir_mapa'),(False,'sfx_zoom_entrar_zona')):
    for i in range(1,6):
        y,l,p=barrido(1000*i+(7 if sube else 3),sube)
        sf.write(f'{nom}_{i}.wav',y,SR,subtype='PCM_24')
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{nom}_{i}.wav','-c:a','libvorbis','-q:a','6',f'{nom}_{i}.ogg'],check=True)
        print(f'{nom}_{i}: {l:.1f} LUFS, pico {p:.1f} dBFS')
