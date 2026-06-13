---
entity_id: "gene.b4613"
entity_type: "gene"
name: "dinQ"
source_database: "NCBI RefSeq"
source_id: "gene-b4613"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4613"
  - "dinQ"
---

# dinQ

`gene.b4613`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4613`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dinQ (gene.b4613) is a gene entity. It encodes dinQ (protein.A5A624). Encoded protein function: Uncharacterized protein DinQ EcoCyc product frame: MONOMER0-1941. Genomic coordinates: 3647705-3647788. EcoCyc protein note: dinQ encodes a small (27 amino acid) toxic protein that localises to the inner membrane in E. coli K-12. DinQ is predicted to contain a single transmembrane region. dinQ-agrAB may be a type I toxin-antitoxin system in E.coli K-12 . dinQ expression is controlled by the RNA0-380 "AgrB small RNA". The agrB transcript counteracts the UV sensitivity induced by dinQ expression. The two small non-coding RNAs - agrA and agrB - both contain a region of antisense complementarity to dinQ . The phenotype of augmented DinQ in an agrB deleted strain has been studied. DinQ is involved in nucleoid compaction and reorganisation during UV exposure. DinQ modulates conjugal recombination. Overexpression of dinQ depolarises the cell membrane and decreases the intracellular ATP concentration . A dinQ ORF of 150 bp was previously annotated. later reported that biologically active DinQ is translated from post-transcriptionally modified dinQ RNA. dinQ is translated from an alternate GTG start codon . Expression of dinQ is DNA damage-inducible and appears to be regulated by LexA . dinQ: damage inducible protein

## Biological Role

Repressed by glaR (protein.P37338). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.A5A624|protein.A5A624]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dinQ; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=dinQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ECOCYC:G0-9981,GeneID:5061522`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3647705-3647788:-; feature_type=gene
