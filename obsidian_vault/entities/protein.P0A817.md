---
entity_id: "protein.P0A817"
entity_type: "protein"
name: "metK"
source_database: "UniProt"
source_id: "P0A817"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00086}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metK metX b2942 JW2909"
---

# metK

`protein.P0A817`

## Static

- Type: `protein`
- Source: `UniProt:P0A817`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00086}.

## Enriched Summary

FUNCTION: Catalyzes the formation of S-adenosylmethionine (AdoMet) from methionine and ATP. The overall synthetic reaction is composed of two sequential steps, AdoMet formation and the subsequent tripolyphosphate hydrolysis which occurs prior to release of AdoMet from the enzyme (PubMed:10551856, PubMed:10660564, PubMed:6251075, PubMed:7629147, PubMed:7629176, PubMed:9753435). Is essential for growth (PubMed:11952912). {ECO:0000269|PubMed:10551856, ECO:0000269|PubMed:10660564, ECO:0000269|PubMed:11952912, ECO:0000269|PubMed:6251075, ECO:0000269|PubMed:7629147, ECO:0000269|PubMed:7629176, ECO:0000269|PubMed:9753435}. Methionine adenosyltransferase catalyzes the formation of the sulfonium compound S-adenosylmethionine. The reaction is unusual in that the entire tripolyphosphate chain is cleaved from the ATP molecule, and is further degraded to pyrophosphate and phosphate before the products are released . Due to its importance, the enzyme is a target for the development of antimicrobial and anticancer compounds. The enzyme is a homotetramer in solution ; the tetrameric form is required for activity . Various crystal structures of methionine adenosyltransferase have been solved. The enzyme is a dimer of dimers with active sites located at the dimer interfaces . A mobile loop gates access to the active site...

## Biological Role

Catalyzes ATP:L-methionine S-adenosyltransferase (reaction.R00177). Component of methionine adenosyltransferase (complex.ecocyc.S-ADENMETSYN-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of S-adenosylmethionine (AdoMet) from methionine and ATP. The overall synthetic reaction is composed of two sequential steps, AdoMet formation and the subsequent tripolyphosphate hydrolysis which occurs prior to release of AdoMet from the enzyme (PubMed:10551856, PubMed:10660564, PubMed:6251075, PubMed:7629147, PubMed:7629176, PubMed:9753435). Is essential for growth (PubMed:11952912). {ECO:0000269|PubMed:10551856, ECO:0000269|PubMed:10660564, ECO:0000269|PubMed:11952912, ECO:0000269|PubMed:6251075, ECO:0000269|PubMed:7629147, ECO:0000269|PubMed:7629176, ECO:0000269|PubMed:9753435}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00177|reaction.R00177]] `KEGG` `database` - via EC:2.5.1.6
- `is_component_of` --> [[complex.ecocyc.S-ADENMETSYN-CPLX|complex.ecocyc.S-ADENMETSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2942|gene.b2942]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A817`
- `KEGG:ecj:JW2909;eco:b2942;ecoc:C3026_16105;`
- `GeneID:86861032;93779055;945389;`
- `GO:GO:0000287; GO:0004478; GO:0005524; GO:0005829; GO:0006556; GO:0006730; GO:0030955; GO:0033353; GO:0042802`
- `EC:2.5.1.6`

## Notes

S-adenosylmethionine synthase (AdoMet synthase) (EC 2.5.1.6) (MAT) (Methionine adenosyltransferase)
