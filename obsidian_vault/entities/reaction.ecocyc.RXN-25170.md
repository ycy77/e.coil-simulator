---
entity_id: "reaction.ecocyc.RXN-25170"
entity_type: "reaction"
name: "RXN-25170"
source_database: "EcoCyc"
source_id: "RXN-25170"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25170

`reaction.ecocyc.RXN-25170`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25170`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Octanoylated-domains + S-ADENOSYLMETHIONINE + Lipoyl-Synthase-Carrying-2-Fe4-S4-Clusters + PROTON + Reduced-ferredoxins -> Dihydro-Lipoyl-Proteins + CH33ADO + MET + Lipoyl-Synthase-Carrying-an-Fe4-S4-Cluster + CPD-7046 + FE+2 + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Octanoylated-domains + S-ADENOSYLMETHIONINE + Lipoyl-Synthase-Carrying-2-Fe4-S4-Clusters + PROTON + Reduced-ferredoxins -> Dihydro-Lipoyl-Proteins + CH33ADO + MET + Lipoyl-Synthase-Carrying-an-Fe4-S4-Cluster + CPD-7046 + FE+2 + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: S-Adenosyl-L-methionine (molecule.C00019), H+ (molecule.C00080), a [lipoyl-carrier protein] N6-octanoyl-L-lysine (molecule.ecocyc.Octanoylated-domains). Products: L-Methionine (molecule.C00073), Fe2+ (molecule.C14818), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO), S2- (molecule.ecocyc.CPD-7046), a [lipoyl-carrier protein]-N6-[(R)-dihydrolipoyl]-L-lysine (molecule.ecocyc.Dihydro-Lipoyl-Proteins).

## Annotation

Octanoylated-domains + S-ADENOSYLMETHIONINE + Lipoyl-Synthase-Carrying-2-Fe4-S4-Clusters + PROTON + Reduced-ferredoxins -> Dihydro-Lipoyl-Proteins + CH33ADO + MET + Lipoyl-Synthase-Carrying-an-Fe4-S4-Cluster + CPD-7046 + FE+2 + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-7046|molecule.ecocyc.CPD-7046]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Dihydro-Lipoyl-Proteins|molecule.ecocyc.Dihydro-Lipoyl-Proteins]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Octanoylated-domains|molecule.ecocyc.Octanoylated-domains]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25170`

## Notes

Octanoylated-domains + S-ADENOSYLMETHIONINE + Lipoyl-Synthase-Carrying-2-Fe4-S4-Clusters + PROTON + Reduced-ferredoxins -> Dihydro-Lipoyl-Proteins + CH33ADO + MET + Lipoyl-Synthase-Carrying-an-Fe4-S4-Cluster + CPD-7046 + FE+2 + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT
