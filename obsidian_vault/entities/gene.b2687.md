---
entity_id: "gene.b2687"
entity_type: "gene"
name: "luxS"
source_database: "NCBI RefSeq"
source_id: "gene-b2687"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2687"
  - "luxS"
---

# luxS

`gene.b2687`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2687`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

luxS (gene.b2687) is a gene entity. It encodes luxS (protein.P45578). Encoded protein function: FUNCTION: Involved in the synthesis of autoinducer 2 (AI-2) which is secreted by bacteria and is used to communicate both the cell density and the metabolic potential of the environment. The regulation of gene expression in response to changes in cell density is called quorum sensing. Catalyzes the transformation of S-ribosylhomocysteine (RHC) to homocysteine (HC) and 4,5-dihydroxy-2,3-pentadione (DPD). {ECO:0000269|PubMed:9618536, ECO:0000269|PubMed:9990077}. EcoCyc product frame: EG12712-MONOMER. EcoCyc synonyms: ygaG. Genomic coordinates: 2814218-2814733. EcoCyc protein note: LuxS is involved in biosynthesis of AI-2, the hormone-like signal that mediates cell-cell communication during quorum sensing, the response to increased cell density . LuxS is the synthase that catalyzes formation of AI-2 by cleavage of S-ribosylhomocysteine . LuxS also participates in recycling of S-adenosylhomocysteine via the PWY-6151 . Stochastic modelling has predicted an alternative pathway for AI-2 formation . It was later found that AI-2 can form spontaneously from ribulose-5-phosphate, but this reaction may not be relevant in wild type E. coli . A catalytic mechanism for LuxS has been proposed...

## Biological Role

Repressed by cyaR (gene.b4438). Activated by uvrY (protein.P0AED5), rpoS (protein.P13445).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45578|protein.P45578]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AED5|protein.P0AED5]] `RegulonDB` `S` - regulator=UvrY; target=luxS; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=luxS; function=+
- `represses` <-- [[gene.b4438|gene.b4438]] `RegulonDB` `S` - regulator=CyaR; target=luxS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008842,ECOCYC:EG12712,GeneID:947168`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2814218-2814733:-; feature_type=gene
