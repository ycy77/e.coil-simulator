---
entity_id: "molecule.C00670"
entity_type: "small_molecule"
name: "sn-Glycero-3-phosphocholine"
source_database: "KEGG"
source_id: "C00670"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "sn-Glycero-3-phosphocholine"
  - "Glycerophosphocholine"
  - "sn-3-GPC"
  - "glycero-phosphocholine"
  - "L-1-glycero-3-phosphocholine"
  - "L-1-glycero-phosphorylcholine"
  - "choline alfoscerate"
---

# sn-Glycero-3-phosphocholine

`molecule.C00670`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00670`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: sn-Glycero-3-phosphocholine; Glycerophosphocholine

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00565` Ether lipid metabolism (KEGG)

## Annotation

KEGG compound: sn-Glycero-3-phosphocholine; Glycerophosphocholine

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00565` Ether lipid metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R01309|reaction.R01309]] `KEGG` `database` - C00157 + 2 C00001 <=> C00670 + 2 C00162
- `is_product_of` --> [[reaction.R07291|reaction.R07291]] `KEGG` `database` - C04230 + C00001 <=> C00670 + C00060
- `is_product_of` --> [[reaction.ecocyc.LYSOPHOSPHOLIPASE-RXN|reaction.ecocyc.LYSOPHOSPHOLIPASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16225|reaction.ecocyc.RXN-16225]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00670`
- `EcoCyc:L-1-GLYCERO-PHOSPHORYLCHOLINE`
- `HMDB:HMDB0000086`
- `ZINC:ZINC000001532714`
- `REACTOME-CPD:1498750`
- `SEED:cpd00507`
- `METANETX:MNXM367`
- `REFMET:sn-glycero-3-phosphocholine`
- `BIGG:g3pc`
- `CHEBI:16870`
- `LIGAND-CPD:D07349`
- `PUBCHEM:657272`
- `canonicalized_from:molecule.ecocyc.L-1-GLYCERO-PHOSPHORYLCHOLINE`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.L-1-GLYCERO-PHOSPHORYLCHOLINE: EcoCyc:L-1-GLYCERO-PHOSPHORYLCHOLINE
