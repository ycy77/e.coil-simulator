---
entity_id: "protein.P05804"
entity_type: "protein"
name: "uidA"
source_database: "UniProt"
source_id: "P05804"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uidA gurA gusA b1617 JW1609"
---

# uidA

`protein.P05804`

## Static

- Type: `protein`
- Source: `UniProt:P05804`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Displays beta-glucuronidase activity with the artificial substrate p-nitrophenyl-beta-D-glucuronide (PNPG) and with 4-methylumbelliferyl-glucuronide (PubMed:21051639, PubMed:23690068, PubMed:26364932, PubMed:3105604, PubMed:33664385). Is likely capable of scavenging glucuronate from a range of chemically distinct xenobiotic and endobiotic glucuronides present in the gastrointestinal (GI) tract, to be able to utilize these diverse sources of carbon. As part of the GI microbiome, this enzyme is able to reactivate glucuronide drug conjugates, such reactivated compounds can significantly damage the GI tract (PubMed:26364932). {ECO:0000269|PubMed:21051639, ECO:0000269|PubMed:23690068, ECO:0000269|PubMed:26364932, ECO:0000269|PubMed:3105604, ECO:0000269|PubMed:33664385}. β-D-glucuronidase catalyzes the cleavage of a wide variety of β-glucuronides . The enzyme is a homotetramer , but higher-order multimers have also been shown to be active . A number of crystal structures of the enzyme alone and bound to specific inhibitors have been solved . Reaction kinetics of single molecules have been measured and compared to values measured in bulk assays . β-D-glucuronidase and BETAGALACTOSID-CPLX belong to the same protein family and thus probably share a common evolutionary ancestor . Wild-type β-D-glucuronidase has very weak β-galactosidase activity...

## Biological Role

Component of β-D-glucuronidase (complex.ecocyc.CPLX0-7662).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Displays beta-glucuronidase activity with the artificial substrate p-nitrophenyl-beta-D-glucuronide (PNPG) and with 4-methylumbelliferyl-glucuronide (PubMed:21051639, PubMed:23690068, PubMed:26364932, PubMed:3105604, PubMed:33664385). Is likely capable of scavenging glucuronate from a range of chemically distinct xenobiotic and endobiotic glucuronides present in the gastrointestinal (GI) tract, to be able to utilize these diverse sources of carbon. As part of the GI microbiome, this enzyme is able to reactivate glucuronide drug conjugates, such reactivated compounds can significantly damage the GI tract (PubMed:26364932). {ECO:0000269|PubMed:21051639, ECO:0000269|PubMed:23690068, ECO:0000269|PubMed:26364932, ECO:0000269|PubMed:3105604, ECO:0000269|PubMed:33664385}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7662|complex.ecocyc.CPLX0-7662]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1617|gene.b1617]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05804`
- `KEGG:ecj:JW1609;eco:b1617;ecoc:C3026_09300;`
- `GeneID:93775766;946149;`
- `GO:GO:0004566; GO:0005829; GO:0005975; GO:0030246; GO:0032991; GO:0042802`
- `EC:3.2.1.31`

## Notes

Beta-glucuronidase (GUS) (EC 3.2.1.31) (Beta-D-glucuronoside glucuronosohydrolase) (EcGUS) (UID)
