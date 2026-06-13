---
entity_id: "reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN"
entity_type: "reaction"
name: "6-PHOSPHO-BETA-GLUCOSIDASE-RXN"
source_database: "EcoCyc"
source_id: "6-PHOSPHO-BETA-GLUCOSIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 6-PHOSPHO-BETA-GLUCOSIDASE-RXN

`reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:6-PHOSPHO-BETA-GLUCOSIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ALSO HYDROLYSES SEVERAL OTHER PHOSPHO-β-D-GLUCOSIDES, BUT NOT THEIR NON-PHOSPHORYLATED FORMS. EcoCyc reaction equation: CPD-15978 + WATER -> D-glucopyranose-6-phosphate + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT. ALSO HYDROLYSES SEVERAL OTHER PHOSPHO-β-D-GLUCOSIDES, BUT NOT THEIR NON-PHOSPHORYLATED FORMS.

## Biological Role

Catalyzed by monoacetylchitobiose-6-phosphate hydrolase (complex.ecocyc.CPLX0-7979), bglB (protein.P11988), ascB (protein.P24240). Substrates: H2O (molecule.C00001), D-cellobiose 6'-phosphate (molecule.ecocyc.CPD-15978). Products: D-Glucose (molecule.C00031), D-Glucose 6-phosphate (molecule.C00092).

## Annotation

ALSO HYDROLYSES SEVERAL OTHER PHOSPHO-β-D-GLUCOSIDES, BUT NOT THEIR NON-PHOSPHORYLATED FORMS.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7979|complex.ecocyc.CPLX0-7979]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P11988|protein.P11988]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P24240|protein.P24240]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15978|molecule.ecocyc.CPD-15978]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:6-PHOSPHO-BETA-GLUCOSIDASE-RXN`

## Notes

CPD-15978 + WATER -> D-glucopyranose-6-phosphate + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT
