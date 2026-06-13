---
entity_id: "gene.b0762"
entity_type: "gene"
name: "acrZ"
source_database: "NCBI RefSeq"
source_id: "gene-b0762"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0762"
  - "acrZ"
---

# acrZ

`gene.b0762`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0762`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acrZ (gene.b0762) is a gene entity. It encodes acrZ (protein.P0AAW9). Encoded protein function: FUNCTION: Accessory component of the AcrABZ-TolC efflux protein complex, which has a broad substrate specificity (PubMed:23010927, PubMed:24747401, PubMed:28355133, PubMed:32348749). Binds to AcrB and perhaps together with membrane lipids, such as cardiolipin, influences the specificity of substrate export (PubMed:23010927, PubMed:24747401, PubMed:28355133, PubMed:32348749). {ECO:0000269|PubMed:23010927, ECO:0000269|PubMed:24747401, ECO:0000269|PubMed:28355133, ECO:0000269|PubMed:32348749}. EcoCyc product frame: G6396-MONOMER. EcoCyc synonyms: ybhT. Genomic coordinates: 794773-794922. EcoCyc protein note: acrZ encodes a small membrane protein that associates with the TRANS-CPLX-201 AcrAB-TolC multidrug efflux pump in an AcrB-dependent manner. AcrZ affects the substrate specificity of the AcrAB-TolC efflux pump . AcrZ and membrane lipids may modulate the activity of AcrB through allosteric changes . AcrZ with a sequential peptide affinity tag (AcrZ-SPA) interacts specifically with AcrB. AcrZ is required for efflux of some AcrB susbtrates (puromycin, chloramphenicol, tetracycline) but not others (erythromycin, rifampicin, fusidic acid) . AcrZ adopts a hydrophobic α-helical structure that fits into a groove in the transmembrane domain of AcrB...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAW9|protein.P0AAW9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=acrZ; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002595,ECOCYC:G6396,GeneID:945365`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:794773-794922:+; feature_type=gene
