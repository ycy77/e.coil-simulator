---
entity_id: "gene.b4391"
entity_type: "gene"
name: "ettA"
source_database: "NCBI RefSeq"
source_id: "gene-b4391"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4391"
  - "ettA"
---

# ettA

`gene.b4391`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4391`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ettA (gene.b4391) is a gene entity. It encodes ettA (protein.P0A9W3). Encoded protein function: FUNCTION: A translation factor that gates the progression of the 70S ribosomal initiation complex (IC, containing tRNA(fMet) in the P-site) into the translation elongation cycle by using a mechanism sensitive to the ATP/ADP ratio. Binds to the 70S ribosome E-site where it modulates the state of the translating ribosome during subunit translocation. Stimulates dipeptide bond synthesis in the presence of ATP (cell in high energy state), but inhibits dipeptide synthesis in the presence of ADP (cell in low energy state), and thus may control translation in response to changing ATP levels (including during stationary phase). Following ATP hydrolysis is probably released allowing the ribosome to enter the elongation phase. ATPase activity is stimulated in the presence of ribosomes. Its specificity for the IC may be conferred by its recognition of features unique to tRNA(fMet). {ECO:0000269|PubMed:24389465, ECO:0000269|PubMed:24389466}.; FUNCTION: Allows translation of proteins with poly-acidic sequences in the protein N-terminus, which otherwise cause intrinsic ribosome destabilization (IRD) due to difficulties in maintaining an intact ribosome. {ECO:0000269|PubMed:38661232}. EcoCyc product frame: YJJK-MONOMER. EcoCyc synonyms: yjjK. Genomic coordinates: 4628855-4630522...

## Biological Role

Activated by cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9W3|protein.P0A9W3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014400,ECOCYC:EG12343,GeneID:948909`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4628855-4630522:-; feature_type=gene
