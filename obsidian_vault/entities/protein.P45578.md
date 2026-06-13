---
entity_id: "protein.P45578"
entity_type: "protein"
name: "luxS"
source_database: "UniProt"
source_id: "P45578"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "luxS ygaG b2687 JW2662"
---

# luxS

`protein.P45578`

## Static

- Type: `protein`
- Source: `UniProt:P45578`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the synthesis of autoinducer 2 (AI-2) which is secreted by bacteria and is used to communicate both the cell density and the metabolic potential of the environment. The regulation of gene expression in response to changes in cell density is called quorum sensing. Catalyzes the transformation of S-ribosylhomocysteine (RHC) to homocysteine (HC) and 4,5-dihydroxy-2,3-pentadione (DPD). {ECO:0000269|PubMed:9618536, ECO:0000269|PubMed:9990077}. LuxS is involved in biosynthesis of AI-2, the hormone-like signal that mediates cell-cell communication during quorum sensing, the response to increased cell density . LuxS is the synthase that catalyzes formation of AI-2 by cleavage of S-ribosylhomocysteine . LuxS also participates in recycling of S-adenosylhomocysteine via the PWY-6151 . Stochastic modelling has predicted an alternative pathway for AI-2 formation . It was later found that AI-2 can form spontaneously from ribulose-5-phosphate, but this reaction may not be relevant in wild type E. coli . A catalytic mechanism for LuxS has been proposed . The DH5α strain has a luxS mutation that prevents autoinducer production, whereas the MG1655 strain produces autoinducer . The differences between wild type and luxS mutants have been examined by gene expression and phenotype microarrays and by profiling the metabolites of the PWY-6151...

## Biological Role

Catalyzes RIBOSYLHOMOCYSTEINASE-RXN (reaction.ecocyc.RIBOSYLHOMOCYSTEINASE-RXN).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Involved in the synthesis of autoinducer 2 (AI-2) which is secreted by bacteria and is used to communicate both the cell density and the metabolic potential of the environment. The regulation of gene expression in response to changes in cell density is called quorum sensing. Catalyzes the transformation of S-ribosylhomocysteine (RHC) to homocysteine (HC) and 4,5-dihydroxy-2,3-pentadione (DPD). {ECO:0000269|PubMed:9618536, ECO:0000269|PubMed:9990077}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RIBOSYLHOMOCYSTEINASE-RXN|reaction.ecocyc.RIBOSYLHOMOCYSTEINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2687|gene.b2687]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45578`
- `KEGG:ecj:JW2662;eco:b2687;ecoc:C3026_14795;`
- `GeneID:93779324;947168;`
- `GO:GO:0005506; GO:0005829; GO:0009372; GO:0019284; GO:0043768`
- `EC:4.4.1.21`

## Notes

S-ribosylhomocysteine lyase (EC 4.4.1.21) (AI-2 synthesis protein) (Autoinducer-2 production protein LuxS)
