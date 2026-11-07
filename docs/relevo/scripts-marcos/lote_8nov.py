import shutil
CR = chr(13) + chr(10)
NL = chr(10)
BASE = 'C:/Dev/TBD/Assets/TBD/Scripts/View/'
shutil.copy('C:/Dev/mr-mak-workspace/entregas/sonido-noche55/codigo/Sfx.cs', BASE + 'Sfx.cs')


def rw(p, f):
    raw = open(BASE + p, encoding='utf-8', newline='').read()
    crlf = CR in raw
    t = f(raw.replace(CR, NL))
    if crlf:
        t = t.replace(NL, CR)
    open(BASE + p, 'w', encoding='utf-8', newline='').write(t)


def rep(t, a, b, label):
    assert a in t, label
    return t.replace(a, b, 1)


def nt(t):
    # sonidos 3D (Nuria)
    t = rep(t, 'Sfx.Play("sfx_zombi_muerte", 0.3f, 0.2f, 0.9f + (_nightKills % 5) * 0.04f);', 'if (UnityEngine.Random.Range(0, 10) == 0) Sfx.PlayAt("zombi_caida", new Vector3(zs[i].Pos.x, 0.3f, zs[i].Pos.z), 0.3f, 0.25f);', 'muerte')
    i = t.index('            if (hits.Count > 0 && _orthoSize < 14f) { Sfx.Play("impacto_carne"')
    j = t.index(NL, i)
    t = t[:i] + '            // (los sonidos 2D de impacto/caida/muerte se quitan: Nuria, zombi_caida 3D en KillZombies)' + t[j:]
    t = rep(t, 'Sfx.Play("explosion_granada", Vector3.zero, 0.7f, 0.3f);', 'Sfx.PlayAt("explosion_granada", new Vector3(s.AimX / 1000f, 0.5f, s.AimY / 1000f), 0.7f, 0.3f);', 'granada')
    t = rep(t, 'Sfx.Play("cola_urbana", Vector3.zero, 0.3f, 0.4f);', 'Sfx.PlayAt("cola_urbana", new Vector3(man.X / 1000f, 1.2f, man.Y / 1000f), 0.3f, 0.4f);', 'cola')
    # estrellas fuera
    t = rep(t, '            _endStars = stars;', '            _endStars = 0;                                                           // D-N149: sin estrellas', 'stars')
    i = t.index('                if (won) sbb.AppendLine($"estrellas')
    j = t.index(NL, i)
    t = t[:i] + t[j + 1:]
    t = rep(t, '"06:00. Amanece en Sagunto.' + chr(92) + 'nLa estación resiste."', '"Sagunto resiste.' + chr(92) + 'nSe sigue en el mundo."', 'resiste') if ('"06:00. Amanece en Sagunto.' + chr(92) + 'nLa estación resiste."') in t else t
    # pausa en silencio
    t = rep(t, '            ColorCases();' + NL, '            AudioListener.pause = _paused && _nightOn;                                // al pausar se silencia todo (Eugenio)' + NL + '            ColorCases();' + NL, 'pausa')
    return t


rw('PrototypeBootstrap.Night.cs', nt)


def vh(t):
    t = rep(t, 'Sfx.Play("impacto_30mm", Vector3.zero, 0.7f, 0.5f); Sfx.Play("cola_urbana", Vector3.zero, 0.4f, 0.5f);', 'Sfx.PlayAt("impacto_30mm", new Vector3(tp.x, 0.5f, tp.y), 0.7f, 0.5f); Sfx.PlayAt("cola_urbana", new Vector3(v.Pos.x, v.Alt + 2f, v.Pos.y), 0.4f, 0.5f);', 'impacto30')
    return t


rw('PrototypeBootstrap.Vehicles.cs', vh)


def fx(t):
    t = rep(t, '0.22f * (1f - 0.85f * far01), false);', '0.10f * (1f - 0.85f * far01), false);', 'amb')
    t = rep(t, '0.10f * far01, false);', '0.05f * far01, false);', 'viento')
    t = rep(t, 'o < 12f ? 0.22f * hv : 0f', 'o < 12f ? 0.10f * hv : 0f', 'horda')
    t = rep(t, 'new Vector3(110f, 0f, 64.5f), 0.25f, 60f)', 'new Vector3(110f, 0f, 64.5f), 0.12f, 60f)', 'tren')
    t = rep(t, 'p3, 0.5f * v.Rpm, 200f);', 'p3, 0.22f * v.Rpm, 200f);', 'rotor')
    t = rep(t, 'Mathf.Abs(v.Speed) > 0.5f ? 0.5f : 0f, 60f);', 'Mathf.Abs(v.Speed) > 0.5f ? 0.25f : 0f, 60f);', 'motor')
    return t


rw('PrototypeBootstrap.Fx.cs', fx)


def ps(t):
    t = rep(t, 'Sfx.Loop("sfx_batalla_mapa_1", s.Sim.Night.State == NightState.Jugando ? 0.3f : 0f, false);', 'Sfx.Loop("sfx_batalla_mapa_1", s.Sim.Night.State == NightState.Jugando ? 0.15f : 0f, false);', 'batalla')
    return t


rw('PrototypeBootstrap.Persist.cs', ps)


def orders(t):
    # recuadro de seleccion visible al arrastrar
    a = '            // formacion activa'
    assert a in t
    new = '''            // recuadro de seleccion al arrastrar con el boton izquierdo (hueso, relleno tenue), por encima del mundo
            if (_selDrag && UnityEngine.InputSystem.Mouse.current != null && UnityEngine.InputSystem.Mouse.current.leftButton.isPressed)
            {
                var mpq = UnityEngine.InputSystem.Mouse.current.position.ReadValue(); var ds = mpq - _selStart;
                if (ds.magnitude > 6f)
                {
                    float x0 = Mathf.Min(_selStart.x, mpq.x), x1 = Mathf.Max(_selStart.x, mpq.x), y0 = Screen.height - Mathf.Max(_selStart.y, mpq.y), y1 = Screen.height - Mathf.Min(_selStart.y, mpq.y);
                    OvEnsure(); var oldc = GUI.color; GUI.color = new Color(OvHueso.r, OvHueso.g, OvHueso.b, 0.12f); GUI.DrawTexture(Rect.MinMaxRect(x0, y0, x1, y1), _ovTex); GUI.color = oldc;
                    OvLine(new Vector2(x0, y0), new Vector2(x1, y0), 2f, OvHueso, 0.95f); OvLine(new Vector2(x0, y1), new Vector2(x1, y1), 2f, OvHueso, 0.95f);
                    OvLine(new Vector2(x0, y0), new Vector2(x0, y1), 2f, OvHueso, 0.95f); OvLine(new Vector2(x1, y0), new Vector2(x1, y1), 2f, OvHueso, 0.95f);
                }
            }
'''
    return t.replace(a, new + a, 1)


rw('PrototypeBootstrap.Orders.cs', orders)


def pb(t):
    a = 'if (notches < 0f && _targetOrtho >= 69.5f && _zoneNode >= 0 && !NightRun.Active)'
    assert a in t
    return t.replace(a, 'if (notches < 0f && _targetOrtho >= 69.5f && _zoneNode >= 0)', 1)


rw('PrototypeBootstrap.cs', pb)
print('ok')
