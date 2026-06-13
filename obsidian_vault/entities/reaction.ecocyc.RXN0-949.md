---
entity_id: "reaction.ecocyc.RXN0-949"
entity_type: "reaction"
name: "RXN0-949"
source_database: "EcoCyc"
source_id: "RXN0-949"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-949

`reaction.ecocyc.RXN0-949`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-949`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + Octanoylated-domains + Fe4S4-Cluster-Protein + Reduced-ferredoxins + PROTON -> Dihydro-Lipoyl-Proteins + CH33ADO + MET + Iron-Sulfur-Cluster-Scaffold-Proteins + CPD-7046 + FE+2 + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Octanoylated-domains + Fe4S4-Cluster-Protein + Reduced-ferredoxins + PROTON -> Dihydro-Lipoyl-Proteins + CH33ADO + MET + Iron-Sulfur-Cluster-Scaffold-Proteins + CPD-7046 + FE+2 + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lipoyl synthase (complex.ecocyc.CPLX0-782). Substrates: S-Adenosyl-L-methionine (molecule.C00019), H+ (molecule.C00080), a [lipoyl-carrier protein] N6-octanoyl-L-lysine (molecule.ecocyc.Octanoylated-domains). Products: L-Methionine (molecule.C00073), Fe2+ (molecule.C14818), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO), S2- (molecule.ecocyc.CPD-7046), a [lipoyl-carrier protein]-N6-[(R)-dihydrolipoyl]-L-lysine (molecule.ecocyc.Dihydro-Lipoyl-Proteins).

## Enriched Pathways

- `ecocyc.PWY0-1275` lipoate biosynthesis and incorporation II (EcoCyc)
- `ecocyc.PWY0-501` lipoate biosynthesis and incorporation I (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + Octanoylated-domains + Fe4S4-Cluster-Protein + Reduced-ferredoxins + PROTON -> Dihydro-Lipoyl-Proteins + CH33ADO + MET + Iron-Sulfur-Cluster-Scaffold-Proteins + CPD-7046 + FE+2 + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1275` lipoate biosynthesis and incorporation II (EcoCyc)
- `ecocyc.PWY0-501` lipoate biosynthesis and incorporation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-782|complex.ecocyc.CPLX0-782]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-7046|molecule.ecocyc.CPD-7046]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Dihydro-Lipoyl-Proteins|molecule.ecocyc.Dihydro-Lipoyl-Proteins]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Octanoylated-domains|molecule.ecocyc.Octanoylated-domains]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-949`

## Notes

S-ADENOSYLMETHIONINE + Octanoylated-domains + Fe4S4-Cluster-Protein + Reduced-ferredoxins + PROTON -> Dihydro-Lipoyl-Proteins + CH33ADO + MET + Iron-Sulfur-Cluster-Scaffold-Proteins + CPD-7046 + FE+2 + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT
