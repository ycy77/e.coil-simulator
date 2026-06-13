---
entity_id: "gene.b2706"
entity_type: "gene"
name: "gutM"
source_database: "NCBI RefSeq"
source_id: "gene-b2706"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2706"
  - "gutM"
---

# gutM

`gene.b2706`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2706`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gutM (gene.b2706) is a gene entity. It encodes gutM (protein.P15081). Encoded protein function: FUNCTION: Positive regulator for glucitol operon expression. EcoCyc product frame: PD00345. EcoCyc synonyms: gut, srlM. Genomic coordinates: 2828621-2828980. EcoCyc protein note: The "glucitol regulator," GutM, is a DNA-binding transcription factor that regulates an operon (gut) involved in transport and utilization of glucitol . This regulator is located in the unusual gut operon, which contains two glucitol-specific transcription factors, GutR and GutM, that regulate this operon negatively and positively, respectively; both regulators control transcription of glucitol PTS permease . Expression of gutM is increased in the presence of glucitol and in the absence of glucose. Although GutM binding does not depend on the presence of glucitol, this compound appears to be necessary for derepressing gutM, perhaps by interacting with GutR . To activate transcription, GutM recognizes DNA-binding sites, but no consensus sequence has been identified. When this protein activates genes involved in glucitol transport and utilization, it appears to bind to their regulatory regions without a coeffector . In addition, Yamada et al...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15081|protein.P15081]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gutM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008898,ECOCYC:EG10972,GeneID:948938`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2828621-2828980:+; feature_type=gene
