---
entity_id: "gene.b3336"
entity_type: "gene"
name: "bfr"
source_database: "NCBI RefSeq"
source_id: "gene-b3336"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3336"
  - "bfr"
---

# bfr

`gene.b3336`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3336`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bfr (gene.b3336) is a gene entity. It encodes bfr (protein.P0ABD3). Encoded protein function: FUNCTION: Iron-storage protein, whose ferroxidase center binds Fe(2+), oxidizes it using dioxygen to Fe(3+), and participates in the subsequent Fe(3+) oxide mineral core formation within the central cavity of the BFR protein shell. The mineralized iron core can contain as many as 2700 iron atoms/24-meric molecule. {ECO:0000269|PubMed:10769150, ECO:0000269|PubMed:14636073}. EcoCyc product frame: EG10113-MONOMER. Genomic coordinates: 3466249-3466725. EcoCyc protein note: bfr encodes the iron storage hemoprotein bacterioferritin . Bacterioferritin and CPLX0-3969 ferritin are distantly related . Under normal growth conditions, bacterioferritin contains approximately 15% of the cell's iron, with 70% of iron found in SUPEROX-DISMUTFE-MONOMER SodB; when cells are grown at high extracellular iron concentration, ferritin stores the bulk of the iron . Notably, a bfr mutant does not exhibit a defect in iron storage . Bacterioferritin exists as a 24-subunit homomultimer that forms a hollow sphere of 95 Å or 119 to 128 Å in diameter. Structural and physical characteristics of Bfr and Bfr complexes have been examined in detail . A homodimeric form of Bfr is favored under low pH conditions . Minimizing salt concentration combined with adjusting the pH to 8...

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), nac (protein.Q47005).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABD3|protein.P0ABD3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=bfr; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=bfr; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010903,ECOCYC:EG10113,GeneID:947839`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3466249-3466725:-; feature_type=gene
