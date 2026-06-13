---
entity_id: "gene.b1533"
entity_type: "gene"
name: "eamA"
source_database: "NCBI RefSeq"
source_id: "gene-b1533"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1533"
  - "eamA"
---

# eamA

`gene.b1533`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1533`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eamA (gene.b1533) is a gene entity. It encodes eamA (protein.P31125). Encoded protein function: FUNCTION: May be an export pump for cysteine and other metabolites of the cysteine pathway (such as N-acetyl-L-serine (NAS) and O-acetyl-L-serine (OAS)), and for other amino acids and their metabolites. {ECO:0000269|PubMed:10844694, ECO:0000269|Ref.6}. EcoCyc product frame: EG11639-MONOMER. EcoCyc synonyms: ydeD. Genomic coordinates: 1620238-1621137. EcoCyc protein note: EamA (formerly YdeD) is an integral membrane protein . EamA is implicated in exporting metabolites of the cysteine pathway; strains overexpressing eamA do not grow on minimal medium with sulfate as the sole sulfur source but do grow when supplemented with L-cystine or with L-methionine plus thiosulfate; strains overexpressing eamA (and grown with L-methionine plus thiosulfate) excrete cysteine, O-acetyl-L-serine and other unidentified compounds* into the culture medium . Overexpression of eamA counteracts the toxicity associated with increased levels of O-acetylserine and increases resistance to the glutamine antagonist, L-AZASERINE; EamA appears to act independently of EG12445-MONOMER "EamB", an alternate O-acetylserine and cysteine efflux permease; EamA may function to modulate O-acetyl-L-serine concentration during exponential growth...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), fur (protein.P0A9A9), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31125|protein.P31125]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=eamA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=eamA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005116,ECOCYC:EG11639,GeneID:946081`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1620238-1621137:-; feature_type=gene
