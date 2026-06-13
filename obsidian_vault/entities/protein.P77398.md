---
entity_id: "protein.P77398"
entity_type: "protein"
name: "arnA"
source_database: "UniProt"
source_id: "P77398"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arnA pmrI yfbG b2255 JW2249"
---

# arnA

`protein.P77398`

## Static

- Type: `protein`
- Source: `UniProt:P77398`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Bifunctional enzyme that catalyzes the oxidative decarboxylation of UDP-glucuronic acid (UDP-GlcUA) to UDP-4-keto-arabinose (UDP-Ara4O) and the addition of a formyl group to UDP-4-amino-4-deoxy-L-arabinose (UDP-L-Ara4N) to form UDP-L-4-formamido-arabinose (UDP-L-Ara4FN). The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:11706007, ECO:0000269|PubMed:15491143, ECO:0000269|PubMed:15695810, ECO:0000269|PubMed:15807526}. ArnA is a bifunctional enzyme that acts within a pathway that modifies lipid A phosphates with 4-amino-4-deoxy-L-arabinose (L-Ara4N), which causes increased resistance to polymyxin . ArnA exhibits UDP-glucuronic acid (UDP-GlcA) C-4"-dehydrogenase and UDP-4-amino-4-deoxy-L-arabinose (UDP-L-Ara4N) formyltransferase activities in vitro . The two activities are separable, and both are required for polymyxin resistance . The N-terminal domain is similar to methionyl-tRNAfMet formyltransferase and catalyzes the N10-formyltetrahydrofolate-dependent formylation of the 4'' amine of UDP-L-Ara4N . Crystal structures of this domain have been solved at 1.7, 1.2 and 2.5 Å resolution . The N10-formyltetrahydrofolate binding site has been identified and a reaction mechanism has been proposed; point mutations in the proposed catalytic residues abolish activity...

## Biological Role

Component of UDP-4-amino-4-deoxy-L-arabinose formyltransferase/UDP-glucuronate dehydrogenase (complex.ecocyc.CPLX0-7718).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Bifunctional enzyme that catalyzes the oxidative decarboxylation of UDP-glucuronic acid (UDP-GlcUA) to UDP-4-keto-arabinose (UDP-Ara4O) and the addition of a formyl group to UDP-4-amino-4-deoxy-L-arabinose (UDP-L-Ara4N) to form UDP-L-4-formamido-arabinose (UDP-L-Ara4FN). The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:11706007, ECO:0000269|PubMed:15491143, ECO:0000269|PubMed:15695810, ECO:0000269|PubMed:15807526}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7718|complex.ecocyc.CPLX0-7718]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2255|gene.b2255]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77398`
- `KEGG:ecj:JW2249;eco:b2255;ecoc:C3026_12595;`
- `GeneID:947683;`
- `GO:GO:0009103; GO:0009245; GO:0016020; GO:0032991; GO:0033320; GO:0042802; GO:0046677; GO:0048040; GO:0070403; GO:0099618; GO:0099619; GO:2001315`
- `EC:1.1.1.305; 2.1.2.13`

## Notes

Bifunctional polymyxin resistance protein ArnA (Polymyxin resistance protein PmrI) [Includes: UDP-4-amino-4-deoxy-L-arabinose formyltransferase (EC 2.1.2.13) (ArnAFT) (UDP-L-Ara4N formyltransferase); UDP-glucuronic acid oxidase, UDP-4-keto-hexauronic acid decarboxylating (EC 1.1.1.305) (ArnADH) (UDP-GlcUA decarboxylase) (UDP-glucuronic acid dehydrogenase)]
