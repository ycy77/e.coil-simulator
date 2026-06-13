---
entity_id: "protein.P69741"
entity_type: "protein"
name: "hybO"
source_database: "UniProt"
source_id: "P69741"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein; Periplasmic side. Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hybO yghV b2997 JW2965"
---

# hybO

`protein.P69741`

## Static

- Type: `protein`
- Source: `UniProt:P69741`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein; Periplasmic side. Periplasm.

## Enriched Summary

FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD2 is involved in hydrogen uptake. HybO is the small subunit of hydrogenase 2; sequence analysis suggests it contains three Fe-S clusters; expected to be two [4Fe-4S] and one [3Fe-4S] as has been shown by x-ray crystallography for the small subunit of a Desulfovibrio gigas [Ni-Fe] hydrogenase . HybO contains a twin-arginine signal sequence which is required for membrane targeting by the Tat system. HybO accumulates in a soluble precursor form in a hypB mutant which is unable to insert nickel into the large subunit (HybC) of hydrogenase 2 . HybO and HybC are coordinately assembled and processed; the presence of both subunits, acquisition of the [Ni-Fe] cofactor and subsequent processing of HybC are required for export of the complex by the Tat system . Review:

## Biological Role

Component of hydrogenase 2 (complex.ecocyc.CPLX0-8762), hydrogenase 2 (complex.ecocyc.FORMHYDROG2-CPLX).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD2 is involved in hydrogen uptake.

## Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8762|complex.ecocyc.CPLX0-8762]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.FORMHYDROG2-CPLX|complex.ecocyc.FORMHYDROG2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2997|gene.b2997]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69741`
- `KEGG:ecj:JW2965;eco:b2997;ecoc:C3026_16390;`
- `GeneID:86861142;93778988;945902;`
- `GO:GO:0005886; GO:0008901; GO:0009055; GO:0009061; GO:0009375; GO:0016020; GO:0033748; GO:0042597; GO:0044569; GO:0046872; GO:0051536; GO:0051538; GO:0051539`
- `EC:1.12.99.6`

## Notes

Hydrogenase-2 small chain (HYD2) (EC 1.12.99.6) (Membrane-bound hydrogenase 2 small subunit) (NiFe hydrogenase)
