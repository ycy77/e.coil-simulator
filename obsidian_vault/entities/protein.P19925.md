---
entity_id: "protein.P19925"
entity_type: "protein"
name: "entD"
source_database: "UniProt"
source_id: "P19925"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Membrane {ECO:0000269|PubMed:2526281}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "entD b0583 JW5085"
---

# entD

`protein.P19925`

## Static

- Type: `protein`
- Source: `UniProt:P19925`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Membrane {ECO:0000269|PubMed:2526281}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. The serine trilactone serves as a scaffolding for the three catechol functionalities that provide hexadentate coordination for the tightly ligated iron(2+) atoms. Plays an essential role in the assembly of the enterobactin by catalyzing the transfer of the 4'-phosphopantetheine (Ppant) moiety from coenzyme A to the apo-domains of both EntB (ArCP domain) and EntF (PCP domain) to yield their holo-forms which make them competent for the activation of 2,3-dihydroxybenzoate (DHB) and L-serine, respectively. {ECO:0000269|PubMed:8939709, ECO:0000269|PubMed:9214294, ECO:0000269|PubMed:9485415}. AcpS is the founding member of a 4'-phosphopantetheinyl (P-pant) transferase protein family that includes E. coli EntD, E. coli o195 protein, and Bacillus subtilis Sfp; family members share two conserved motifs but relatively low sequence identity overall . During enterobactin biosynthesis EntD catalyzes a posttranslational modification by transferring the phosphopantetheinyl moiety of coenzyme A onto a serine side chain in both the C-terminal apo-aryl carrier protein domain of EntB, and a homologous apo-aryl carrier protein domain of EntF...

## Biological Role

Catalyzes ENTDB-RXN (reaction.ecocyc.ENTDB-RXN), RXN-15889 (reaction.ecocyc.RXN-15889). Component of enterobactin synthase (complex.ecocyc.ENTMULTI-CPLX).

## Enriched Pathways

- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. The serine trilactone serves as a scaffolding for the three catechol functionalities that provide hexadentate coordination for the tightly ligated iron(2+) atoms. Plays an essential role in the assembly of the enterobactin by catalyzing the transfer of the 4'-phosphopantetheine (Ppant) moiety from coenzyme A to the apo-domains of both EntB (ArCP domain) and EntF (PCP domain) to yield their holo-forms which make them competent for the activation of 2,3-dihydroxybenzoate (DHB) and L-serine, respectively. {ECO:0000269|PubMed:8939709, ECO:0000269|PubMed:9214294, ECO:0000269|PubMed:9485415}.

## Pathways

- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ENTDB-RXN|reaction.ecocyc.ENTDB-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-15889|reaction.ecocyc.RXN-15889]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.ENTMULTI-CPLX|complex.ecocyc.ENTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0583|gene.b0583]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P19925`
- `KEGG:ecj:JW5085;eco:b0583;`
- `GeneID:945194;`
- `GO:GO:0000287; GO:0008897; GO:0009237; GO:0009239; GO:0009366; GO:0016020`
- `EC:2.7.8.-`

## Notes

Enterobactin synthase component D (4'-phosphopantetheinyl transferase EntD) (EC 2.7.8.-) (Enterochelin synthase D)
