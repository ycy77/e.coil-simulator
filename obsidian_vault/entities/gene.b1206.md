---
entity_id: "gene.b1206"
entity_type: "gene"
name: "dauA"
source_database: "NCBI RefSeq"
source_id: "gene-b1206"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1206"
  - "dauA"
---

# dauA

`gene.b1206`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1206`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dauA (gene.b1206) is a gene entity. It encodes dauA (protein.P0AFR2). Encoded protein function: FUNCTION: Responsible for the aerobic transport of succinate from the periplasm to the cytoplasm at acidic pH (PubMed:23278959). Can transport other C4-dicarboxylic acids such as aspartate and fumarate (PubMed:23278959). May also play a role in the regulation of C4-dicarboxylic acid metabolism at pH 7, via regulation of expression and/or activity of DctA. May act as a co-sensor of DcuS (PubMed:23278959). {ECO:0000269|PubMed:23278959}. EcoCyc product frame: YCHM-MONOMER. EcoCyc synonyms: ychM. Genomic coordinates: 1259124-1260803. EcoCyc protein note: DauA is an inner membrane protein that transports C4 dicarboxylates in an aerobic, acidic (pH 5) environment. DauA transports the monoanion and dianion form of succinate and fumarate, and the dicarboxylic amino acid aspartate. At pH 5, DauA is the main succinate transporter and DCTA-MONOMER "DctA", which is active for dicarboxylate transport at pH 7, is not produced . DauA is required for the optimal expression of DctA at pH 7 . In liquid culture (pH 5) with succinate as the sole carbon source a dauA deletion mutant and a dauA dctA double deletion mutant are unable to grow...

## Biological Role

Repressed by yieP (protein.P31475).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFR2|protein.P0AFR2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P31475|protein.P31475]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004051,ECOCYC:EG12392,GeneID:945770`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1259124-1260803:-; feature_type=gene
