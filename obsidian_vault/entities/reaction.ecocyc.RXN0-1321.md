---
entity_id: "reaction.ecocyc.RXN0-1321"
entity_type: "reaction"
name: "RXN0-1321"
source_database: "EcoCyc"
source_id: "RXN0-1321"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1321

`reaction.ecocyc.RXN0-1321`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1321`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Tgt catalyzes transglycosylation of guanine to 7-aminomethyl-7-deazaguanine (preQ1) in the anticodon loop of tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr). PreQ1 is then converted to epoxyqueuosine (oQ), and then to queuine [Q, 7-(4,5-cis-dihydroxy-2-cyclopenten-1-ylaminomethyl)-7-deazaguanine]. EcoCyc reaction equation: Guanine34-in-tRNAs + 7-AMINOMETHYL-7-DEAZAGUANINE -> tRNA-with-7-aminomethyl-7-deazaguanine + GUANINE; direction=LEFT-TO-RIGHT. Tgt catalyzes transglycosylation of guanine to 7-aminomethyl-7-deazaguanine (preQ1) in the anticodon loop of tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr). PreQ1 is then converted to epoxyqueuosine (oQ), and then to queuine [Q, 7-(4,5-cis-dihydroxy-2-cyclopenten-1-ylaminomethyl)-7-deazaguanine].

## Biological Role

Catalyzed by tRNA-guanine transglycosylase (complex.ecocyc.CPLX0-1101). Substrates: 7-Aminomethyl-7-carbaguanine (molecule.C16675), a guanine34 in tRNA (molecule.ecocyc.Guanine34-in-tRNAs). Products: Guanine (molecule.C00242), a 7-aminomethyl-7-deazaguanosine34 in tRNA (molecule.ecocyc.tRNA-with-7-aminomethyl-7-deazaguanine).

## Enriched Pathways

- `ecocyc.PWY-6700` queuosine biosynthesis I (de novo) (EcoCyc)

## Annotation

Tgt catalyzes transglycosylation of guanine to 7-aminomethyl-7-deazaguanine (preQ1) in the anticodon loop of tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr). PreQ1 is then converted to epoxyqueuosine (oQ), and then to queuine [Q, 7-(4,5-cis-dihydroxy-2-cyclopenten-1-ylaminomethyl)-7-deazaguanine].

## Pathways

- `ecocyc.PWY-6700` queuosine biosynthesis I (de novo) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1101|complex.ecocyc.CPLX0-1101]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00242|molecule.C00242]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-with-7-aminomethyl-7-deazaguanine|molecule.ecocyc.tRNA-with-7-aminomethyl-7-deazaguanine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C16675|molecule.C16675]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Guanine34-in-tRNAs|molecule.ecocyc.Guanine34-in-tRNAs]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-2400|molecule.ecocyc.CPD0-2400]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIMETHYLSUBERIMIDATE|molecule.ecocyc.DIMETHYLSUBERIMIDATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.ETHYLACETIMIDATE|molecule.ecocyc.ETHYLACETIMIDATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.FMPP|molecule.ecocyc.FMPP]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.METHYLMETHANETHIOSULFONATE|molecule.ecocyc.METHYLMETHANETHIOSULFONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-1321`

## Notes

Guanine34-in-tRNAs + 7-AMINOMETHYL-7-DEAZAGUANINE -> tRNA-with-7-aminomethyl-7-deazaguanine + GUANINE; direction=LEFT-TO-RIGHT
