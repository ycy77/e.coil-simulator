---
entity_id: "gene.b0895"
entity_type: "gene"
name: "dmsB"
source_database: "NCBI RefSeq"
source_id: "gene-b0895"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0895"
  - "dmsB"
---

# dmsB

`gene.b0895`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0895`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dmsB (gene.b0895) is a gene entity. It encodes dmsB (protein.P18776). Encoded protein function: FUNCTION: Electron transfer subunit of the terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. EcoCyc product frame: DMSB-MONOMER. Genomic coordinates: 943414-944031. EcoCyc protein note: The DmsB subunit of DMSO reductase subunit contains four 4 (4Fe-4S) clusters - FS1, FS2, FS3 and FS4 .

## Biological Role

Repressed by modE (protein.P0A9G8), narL (protein.P0AF28). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), rpoD (protein.P00579), fur (protein.P0A9A9), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18776|protein.P18776]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dmsB; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=dmsB; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=dmsB; function=+
- `represses` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=dmsB; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=dmsB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003046,ECOCYC:EG10233,GeneID:945507`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:943414-944031:+; feature_type=gene
