---
entity_id: "protein.P0ADI4"
entity_type: "protein"
name: "entB"
source_database: "UniProt"
source_id: "P0ADI4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:10692387}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "entB entG b0595 JW0587"
---

# entB

`protein.P0ADI4`

## Static

- Type: `protein`
- Source: `UniProt:P0ADI4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:10692387}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. The serine trilactone serves as a scaffolding for the three catechol functionalities that provide hexadentate coordination for the tightly ligated iron(3+) atoms. EntB is a bifunctional protein that serves as an isochorismate lyase and an aryl carrier protein (ArCP). Catalyzes the conversion of isochorismate to 2,3-dihydro-2,3-dihydroxybenzoate (2,3-diDHB), the precursor of 2,3-dihydroxybenzoate (DHB). In the enterobactin assembly, EntB functions as an aryl carrier protein phosphopantetheinylated near the C terminus by EntD to yield holo-EntB, which is then acylated by EntE with 2,3-dihydroxybenzoyl-AMP to form DHB-holo-EntB. Then this product will serve in the formation of the amide bond between 2,3-dihydroxybenzoate (DHB) and L-serine. {ECO:0000269|PubMed:16567620, ECO:0000269|PubMed:16632253, ECO:0000269|PubMed:19699210, ECO:0000269|PubMed:2139796, ECO:0000269|PubMed:2172214, ECO:0000269|PubMed:2531000, ECO:0000269|PubMed:9214294, ECO:0000269|PubMed:9485415}. EntB is a bifunctional enzyme that is involved in the enterobactin biosynthesis pathway. Enterobactin, a siderophore molecule, is synthesized in response to iron deprivation by formation of an amide bond between 2,3-dihydroxybenzoate (2,3-DHB) and L-serine...

## Biological Role

Component of 2,3-dihydroxybenzoyl-EntB (complex.ecocyc.CPLX0-7849), holo-EntB dimer (complex.ecocyc.ENTB-CPLX), enterobactin synthase (complex.ecocyc.ENTMULTI-CPLX).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. The serine trilactone serves as a scaffolding for the three catechol functionalities that provide hexadentate coordination for the tightly ligated iron(3+) atoms. EntB is a bifunctional protein that serves as an isochorismate lyase and an aryl carrier protein (ArCP). Catalyzes the conversion of isochorismate to 2,3-dihydro-2,3-dihydroxybenzoate (2,3-diDHB), the precursor of 2,3-dihydroxybenzoate (DHB). In the enterobactin assembly, EntB functions as an aryl carrier protein phosphopantetheinylated near the C terminus by EntD to yield holo-EntB, which is then acylated by EntE with 2,3-dihydroxybenzoyl-AMP to form DHB-holo-EntB. Then this product will serve in the formation of the amide bond between 2,3-dihydroxybenzoate (DHB) and L-serine. {ECO:0000269|PubMed:16567620, ECO:0000269|PubMed:16632253, ECO:0000269|PubMed:19699210, ECO:0000269|PubMed:2139796, ECO:0000269|PubMed:2172214, ECO:0000269|PubMed:2531000, ECO:0000269|PubMed:9214294, ECO:0000269|PubMed:9485415}.

## Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7849|complex.ecocyc.CPLX0-7849]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.ENTB-CPLX|complex.ecocyc.ENTB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.ENTMULTI-CPLX|complex.ecocyc.ENTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `represses` --> [[reaction.ecocyc.ENTDB-RXN|reaction.ecocyc.ENTDB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-15889|reaction.ecocyc.RXN-15889]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b0595|gene.b0595]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADI4`
- `KEGG:ecj:JW0587;eco:b0595;ecoc:C3026_02970;`
- `GeneID:946178;`
- `GO:GO:0000287; GO:0005829; GO:0005886; GO:0008908; GO:0009239; GO:0016765; GO:0031177; GO:0042802; GO:0047527`
- `EC:3.3.2.1; 6.3.2.14`

## Notes

Enterobactin synthase component B (EC 6.3.2.14) (Enterobactin biosynthesis bifunctional protein EntB) (Enterochelin synthase B) [Includes: Isochorismatase (EC 3.3.2.1) (2,3-dihydro-2,3-dihydroxybenzoate synthase) (Isochorismate lyase); Aryl carrier protein (ArCP)]
