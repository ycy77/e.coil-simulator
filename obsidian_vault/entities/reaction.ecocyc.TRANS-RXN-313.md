---
entity_id: "reaction.ecocyc.TRANS-RXN-313"
entity_type: "reaction"
name: "D-alanine:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-313"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-alanine:proton antiport

`reaction.ecocyc.TRANS-RXN-313`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-313`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E. coli K-12 is able to export D-alanine; transport is dependent on the proton electrochemical gradient but the identity of the transport protein is not known. D-alanine accumulates in the extracellular medium of a dadA strain (lacks DALADEHYDROG-CPLX "D-amino acid dehydrogenase") grown in minimal media containing the dipeptide L-Ala-L-Ala. Expression of an alanine racemase (CPLX0-7465 "DadX" or CPLX0-8202 "Alr"), from a plasmid, in this same strain, increases secretion of D-alanine, presumably due to the increased metabolic flow from L-alanine to D-alanine . EcoCyc reaction equation: D-ALANINE + PROTON -> D-ALANINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. E. coli K-12 is able to export D-alanine; transport is dependent on the proton electrochemical gradient but the identity of the transport protein is not known. D-alanine accumulates in the extracellular medium of a dadA strain (lacks DALADEHYDROG-CPLX "D-amino acid dehydrogenase") grown in minimal media containing the dipeptide L-Ala-L-Ala. Expression of an alanine racemase (CPLX0-7465 "DadX" or CPLX0-8202 "Alr"), from a plasmid, in this same strain, increases secretion of D-alanine, presumably due to the increased metabolic flow from L-alanine to D-alanine .

## Biological Role

Substrates: H+ (molecule.C00080), D-Alanine (molecule.C00133). Products: H+ (molecule.C00080), D-Alanine (molecule.C00133).

## Annotation

E. coli K-12 is able to export D-alanine; transport is dependent on the proton electrochemical gradient but the identity of the transport protein is not known. D-alanine accumulates in the extracellular medium of a dadA strain (lacks DALADEHYDROG-CPLX "D-amino acid dehydrogenase") grown in minimal media containing the dipeptide L-Ala-L-Ala. Expression of an alanine racemase (CPLX0-7465 "DadX" or CPLX0-8202 "Alr"), from a plasmid, in this same strain, increases secretion of D-alanine, presumably due to the increased metabolic flow from L-alanine to D-alanine .

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-313`

## Notes

D-ALANINE + PROTON -> D-ALANINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
