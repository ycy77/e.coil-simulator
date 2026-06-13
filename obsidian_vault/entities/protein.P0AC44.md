---
entity_id: "protein.P0AC44"
entity_type: "protein"
name: "sdhD"
source_database: "UniProt"
source_id: "P0AC44"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sdhD b0722 JW0712"
---

# sdhD

`protein.P0AC44`

## Static

- Type: `protein`
- Source: `UniProt:P0AC44`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Membrane-anchoring subunit of succinate dehydrogenase (SDH). One of two membrane proteins in the four subunit enzyme. SdhC and SdhD are the large and small subunits of cytochrome b556, respectively . The b556 type heme bridges both membrane subunits . Published reports disagree about whether mutation of SdhC-[His84] or SdhD-[His71] residues eliminate coordination of the heme b . Mutation of the residues coordinating the heme indicate that the heme helps stabilize the enzyme . SdhC-[His84] is involved in interaction with the quinone electron acceptor . SdhC-[His84] and SdhD-[His71] (with the associated heme b) are reported to be dispensable for assembly, while SdhC-[His30] is required for proper assembly of the membrane-bound enzyme . Mutants lacking SdhC and SdhD show cytoplasmic succinate dehydrogenase activity using artificial electron acceptors, in contrast to wild-type membrane-associated succinate-ubiquinone oxidoreductase activity . Despite similar function, hydrophobicity, and protein size, the SdhC and SdhD subunits of succinate dehydrogenase do not share significant sequence identity with the corresponding membrane-binding subunits of fumarate reductase, FrdC and FrdD . sdhD belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . Regulation has been described .

## Biological Role

Component of succinate:quinone oxidoreductase (complex.ecocyc.CPLX0-8160), succinate:quinone oxidoreductase subcomplex (complex.ecocyc.SUCC-DEHASE).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Membrane-anchoring subunit of succinate dehydrogenase (SDH).

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8160|complex.ecocyc.CPLX0-8160]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.SUCC-DEHASE|complex.ecocyc.SUCC-DEHASE]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0722|gene.b0722]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC44`
- `KEGG:ecj:JW0712;eco:b0722;ecoc:C3026_03615;`
- `GeneID:86863233;93776762;945322;`
- `GO:GO:0005886; GO:0006099; GO:0009055; GO:0009060; GO:0016020; GO:0017004; GO:0019646; GO:0020037; GO:0045273; GO:0046872`

## Notes

Succinate dehydrogenase hydrophobic membrane anchor subunit
