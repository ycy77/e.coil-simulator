---
entity_id: "gene.b0148"
entity_type: "gene"
name: "hrpB"
source_database: "NCBI RefSeq"
source_id: "gene-b0148"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0148"
  - "hrpB"
---

# hrpB

`gene.b0148`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0148`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hrpB (gene.b0148) is a gene entity. It encodes hrpB (protein.P37024). Encoded protein function: ATP-dependent RNA helicase HrpB (EC 3.6.4.13) EcoCyc product frame: EG12329-MONOMER. EcoCyc synonyms: yadO. Genomic coordinates: 162105-164534. EcoCyc protein note: HrpB belongs to the DEAH/RHA subfamily of nucleic acid-dependent NTPases . Nuclease activity of HrpB is highest with CTP and UTP and is stimulated by the presence of single-stranded RNA. HrpB did not show RNA helicase activity with any of the tested substrates . HrpB was initially named based on its similarity to HrpA. However, it differs in that it lacks some conserved residues found in in DEAH-box RNA helicases and HrpA . Crystal structures of HrpB have been solved . The protein comprises a "head" module consisting of two RecA-like domains, a WH domain, an HB domain, and an OB domain, followed by a connector and a unique C-terminal region . In a large genetic interaction screen, hrpB showed genetic interactions with a number of proteins involved in translation . hrpB deletion mutants did not show obvious phenotypes under the tested conditions . The Keio collection hrpB mutant exhibits a 'high level' of resistance to lithium exposure . HrpB: "DEAH-family RNA helicase-like protein B"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37024|protein.P37024]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000510,ECOCYC:EG12329,GeneID:944845`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:162105-164534:+; feature_type=gene
