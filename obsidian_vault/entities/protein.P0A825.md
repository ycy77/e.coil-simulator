---
entity_id: "protein.P0A825"
entity_type: "protein"
name: "glyA"
source_database: "UniProt"
source_id: "P0A825"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00051, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glyA b2551 JW2535"
---

# glyA

`protein.P0A825`

## Static

- Type: `protein`
- Source: `UniProt:P0A825`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00051, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the reversible interconversion of serine and glycine with tetrahydrofolate (THF) serving as the one-carbon carrier. This reaction serves as the major source of one-carbon groups required for the biosynthesis of purines, thymidylate, methionine, and other important biomolecules (PubMed:10858298, PubMed:1517215, PubMed:19883126, PubMed:3891721, PubMed:7925461). Also exhibits THF-independent aldolase activity toward beta-hydroxyamino acids, producing glycine and aldehydes, via a retro-aldol mechanism. Thus, is able to catalyze the cleavage of allothreonine and 3-phenylserine (PubMed:10858298, PubMed:1517215, PubMed:19883126, PubMed:3891721). Also catalyzes the irreversible conversion of 5,10-methenyltetrahydrofolate to 5-formyltetrahydrofolate (PubMed:10858298, PubMed:2201683). {ECO:0000269|PubMed:10858298, ECO:0000269|PubMed:1517215, ECO:0000269|PubMed:19883126, ECO:0000269|PubMed:2201683, ECO:0000269|PubMed:3891721, ECO:0000269|PubMed:7925461}. Serine hydroxymethyltransferase (GlyA) converts L-serine (but not D-serine ) to glycine, transferring a methyl group to tetrahydrofolate, thus forming 5,10-methylene-tetrahydrofolate (5,10-mTHF). 5,10-mTHF is the major source of C1 units in the cell, making GlyA a key enzyme in the biosynthesis of purines, thymidine, methionine, choline and lipids...

## Biological Role

Catalyzes 5,10-methylenetetrahydromethanopterin:glycine hydroxymethyltransferase (reaction.R09099). Component of serine hydroxymethyltransferase (complex.ecocyc.GLYOHMETRANS-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible interconversion of serine and glycine with tetrahydrofolate (THF) serving as the one-carbon carrier. This reaction serves as the major source of one-carbon groups required for the biosynthesis of purines, thymidylate, methionine, and other important biomolecules (PubMed:10858298, PubMed:1517215, PubMed:19883126, PubMed:3891721, PubMed:7925461). Also exhibits THF-independent aldolase activity toward beta-hydroxyamino acids, producing glycine and aldehydes, via a retro-aldol mechanism. Thus, is able to catalyze the cleavage of allothreonine and 3-phenylserine (PubMed:10858298, PubMed:1517215, PubMed:19883126, PubMed:3891721). Also catalyzes the irreversible conversion of 5,10-methenyltetrahydrofolate to 5-formyltetrahydrofolate (PubMed:10858298, PubMed:2201683). {ECO:0000269|PubMed:10858298, ECO:0000269|PubMed:1517215, ECO:0000269|PubMed:19883126, ECO:0000269|PubMed:2201683, ECO:0000269|PubMed:3891721, ECO:0000269|PubMed:7925461}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R09099|reaction.R09099]] `KEGG` `database` - via EC:2.1.2.1
- `is_component_of` --> [[complex.ecocyc.GLYOHMETRANS-CPLX|complex.ecocyc.GLYOHMETRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2551|gene.b2551]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A825`
- `KEGG:ecj:JW2535;eco:b2551;ecoc:C3026_14125;`
- `GeneID:86860671;89517346;947022;`
- `GO:GO:0004372; GO:0005829; GO:0006546; GO:0006564; GO:0006565; GO:0008270; GO:0008732; GO:0016020; GO:0019264; GO:0030170; GO:0035999; GO:0042802; GO:0042803; GO:0046653`
- `EC:2.1.2.1`

## Notes

Serine hydroxymethyltransferase (SHMT) (Serine methylase) (EC 2.1.2.1)
