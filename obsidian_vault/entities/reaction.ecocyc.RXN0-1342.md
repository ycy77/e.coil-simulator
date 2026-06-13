---
entity_id: "reaction.ecocyc.RXN0-1342"
entity_type: "reaction"
name: "RXN0-1342"
source_database: "EcoCyc"
source_id: "RXN0-1342"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1342

`reaction.ecocyc.RXN0-1342`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1342`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The queA gene encodes an S-adenosylmethionine:tRNA ribosyltransferase-isomerase, which catalyzes formation of the 2,3-epoxy-4,5-dihydroxycyclopentane ring of epoxyqueuosine (oQ), a precursor of the queuosine (Q) anticodon loop modification in tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr) . EcoCyc reaction equation: S-ADENOSYLMETHIONINE + tRNA-with-7-aminomethyl-7-deazaguanine -> tRNAs-containing-epoxy-quenosine + ADENINE + MET + PROTON; direction=LEFT-TO-RIGHT. The queA gene encodes an S-adenosylmethionine:tRNA ribosyltransferase-isomerase, which catalyzes formation of the 2,3-epoxy-4,5-dihydroxycyclopentane ring of epoxyqueuosine (oQ), a precursor of the queuosine (Q) anticodon loop modification in tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr) .

## Biological Role

Catalyzed by queA (protein.P0A7F9). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a 7-aminomethyl-7-deazaguanosine34 in tRNA (molecule.ecocyc.tRNA-with-7-aminomethyl-7-deazaguanine). Products: L-Methionine (molecule.C00073), H+ (molecule.C00080), Adenine (molecule.C00147), an epoxyqueuosine34 in tRNA (molecule.ecocyc.tRNAs-containing-epoxy-quenosine).

## Enriched Pathways

- `ecocyc.PWY-6700` queuosine biosynthesis I (de novo) (EcoCyc)

## Annotation

The queA gene encodes an S-adenosylmethionine:tRNA ribosyltransferase-isomerase, which catalyzes formation of the 2,3-epoxy-4,5-dihydroxycyclopentane ring of epoxyqueuosine (oQ), a precursor of the queuosine (Q) anticodon loop modification in tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr) .

## Pathways

- `ecocyc.PWY-6700` queuosine biosynthesis I (de novo) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A7F9|protein.P0A7F9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNAs-containing-epoxy-quenosine|molecule.ecocyc.tRNAs-containing-epoxy-quenosine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-with-7-aminomethyl-7-deazaguanine|molecule.ecocyc.tRNA-with-7-aminomethyl-7-deazaguanine]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.SINEFUNGIN|molecule.ecocyc.SINEFUNGIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-1342`

## Notes

S-ADENOSYLMETHIONINE + tRNA-with-7-aminomethyl-7-deazaguanine -> tRNAs-containing-epoxy-quenosine + ADENINE + MET + PROTON; direction=LEFT-TO-RIGHT
