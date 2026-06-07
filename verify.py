#!/usr/bin/env python3
# Verify the polychord manual: compute actual pitch-class set of (lower triad + upper triad)
# and compare against the claimed chord symbol. Root = C (pitch class 0) throughout.

NOTE = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']

# upper-root interval names -> semitones above root
IV = {'M2':2,'M3':4,'P4':5,'P5':7,'M6':9,'m7':10,'M7':11,'b2/m2':1}

def triad(root_pc, quality):
    if quality=='maj': return {root_pc%12,(root_pc+4)%12,(root_pc+7)%12}
    if quality=='min': return {root_pc%12,(root_pc+3)%12,(root_pc+7)%12}
    if quality=='dim': return {root_pc%12,(root_pc+3)%12,(root_pc+6)%12}

# how to read each semitone as a chord degree (relative to a C root)
DEG = {0:'R',1:'b9',2:'9',3:'m3/#9',4:'M3',5:'11',6:'#11/b5',7:'5',
       8:'b13/#5',9:'13/M6',10:'b7',11:'M7'}

def analyze(lower_q, up_iv, up_q, claim):
    low = triad(0, lower_q)
    up  = triad(IV[up_iv], up_q)
    pcs = sorted(low | up)
    degs = [DEG[p] for p in pcs]
    notes = [NOTE[p] for p in pcs]
    return pcs, notes, degs

rows = [
 # lower, upper-interval, upper-qual, claimed symbol
 ('maj','M2','maj','Xmaj13(#11)'),
 ('maj','M2','min','X13'),
 ('maj','M3','maj','Xmaj7(#5)'),
 ('maj','M3','min','Xmaj7(add5)'),
 ('maj','P4','maj','Xmaj11'),
 ('maj','P4','min','X11(b13)'),
 ('maj','P5','maj','Xmaj9(add13)'),
 ('maj','P5','min','X9'),
 ('maj','M6','maj','Xmaj13(#9)'),
 ('maj','M6','min','Xmaj13'),
 ('maj','m7','maj','X11'),
 ('maj','m7','min','X7(b9,11)'),
 ('maj','M7','maj','Xmaj7(#9,#11)'),
 ('maj','M7','min','Xmaj9(#11)'),
 ('min','M2','maj','Xm9(#11,13)'),
 ('min','M2','min','Xm11(add13)'),
 ('min','M3','maj','Xm(M7,#5)'),
 ('min','M3','min','Xm(M7,add5)'),
 ('min','P4','maj','Xm(add11,13)'),
 ('min','P4','min','Xm11(b13)'),
 ('min','P5','maj','Xm(M7,add9)'),
 ('min','P5','min','Xm9'),
 ('min','M6','maj','Xm(add13,#9)'),
 ('min','M6','min','Xm(add13)'),
 ('min','m7','maj','Xm11'),
 ('min','m7','min','Xm7(b9,11)'),
 ('min','M7','maj','Xm(M7,#9,#11)'),
 ('min','M7','min','Xm(M7,9,#11)'),
]

print(f"{'#':>2}  {'lower':5} {'+up':12} {'claim':18} {'notes (C root)':28} degrees")
print('-'*110)
for i,(lq,iv,uq,claim) in enumerate(rows,1):
    pcs,notes,degs = analyze(lq,iv,uq,claim)
    slug=f"{('X' if lq=='maj' else 'Xm')} + {iv}{uq}"
    print(f"{i:>2}  {lq:5} {slug:12} {claim:18} {' '.join(notes):28} {' '.join(degs)}")

print()
print("=== Locrian special row ===")
low = triad(0,'dim'); up = triad(1,'maj')  # X dim + Db maj (Db = b2)
pcs = sorted(low|up)
print("Xdim + Dbmaj  claim X7(b9,11,b13)")
print("  notes:", ' '.join(NOTE[p] for p in pcs))
print("  degs :", ' '.join(DEG[p] for p in pcs))

print()
print("=== Section-3 mode example labels vs table ===")
checks = [
 ('Dorian','Xm + M6maj','Xm13'),
 ('Aeolian','Xm + M6min','Xm(add13)'),
 ('Phrygian','Xm + M2maj','Xm9(#11,13)'),
]
for mode,combo,label in checks:
    print(f"{mode:9} {combo:14} labeled {label}")
