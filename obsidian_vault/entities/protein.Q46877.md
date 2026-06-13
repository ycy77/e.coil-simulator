---
entity_id: "protein.Q46877"
entity_type: "protein"
name: "norV"
source_database: "UniProt"
source_id: "Q46877"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "norV flrD ygaI ygaJ ygaK b2710 JW2680"
---

# norV

`protein.Q46877`

## Static

- Type: `protein`
- Source: `UniProt:Q46877`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Anaerobic nitric oxide reductase; uses NADH to detoxify nitric oxide (NO), protecting several 4Fe-4S NO-sensitive enzymes. Has at least 2 reductase partners, only one of which (NorW, flavorubredoxin reductase) has been identified. NO probably binds to the di-iron center; electrons enter from the reductase at rubredoxin and are transferred sequentially to the FMN center and the di-iron center. Also able to function as an aerobic oxygen reductase.

## Biological Role

Component of reduced flavorubredoxin (complex.ecocyc.CPLX0-1), oxidized flavorubredoxin (complex.ecocyc.CPLX0-2).

## Annotation

FUNCTION: Anaerobic nitric oxide reductase; uses NADH to detoxify nitric oxide (NO), protecting several 4Fe-4S NO-sensitive enzymes. Has at least 2 reductase partners, only one of which (NorW, flavorubredoxin reductase) has been identified. NO probably binds to the di-iron center; electrons enter from the reductase at rubredoxin and are transferred sequentially to the FMN center and the di-iron center. Also able to function as an aerobic oxygen reductase.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1|complex.ecocyc.CPLX0-1]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` --> [[complex.ecocyc.CPLX0-2|complex.ecocyc.CPLX0-2]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2710|gene.b2710]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46877`
- `KEGG:ecj:JW2680;eco:b2710;ecoc:C3026_14915;`
- `GeneID:948979;`
- `GO:GO:0005506; GO:0005737; GO:0009055; GO:0010181; GO:0016491; GO:0016661; GO:0016966; GO:0032991; GO:0042802; GO:0046210; GO:0071731`

## Notes

Anaerobic nitric oxide reductase flavorubredoxin (FlRd) (FlavoRb)
