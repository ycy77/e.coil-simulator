---
entity_id: "gene.b0215"
entity_type: "gene"
name: "dnaQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0215"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0215"
  - "dnaQ"
---

# dnaQ

`gene.b0215`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0215`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaQ (gene.b0215) is a gene entity. It encodes dnaQ (protein.P03007). Encoded protein function: FUNCTION: DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. The epsilon subunit contain the editing function and is a proofreading 3'-5' exonuclease (PubMed:6340117). Contacts both the beta sliding clamp (dnaN) and the polymerase subunit (dnaE), stabilizing their interaction (PubMed:26499492). {ECO:0000269|PubMed:26499492, ECO:0000269|PubMed:6340117}. EcoCyc product frame: EG10243-MONOMER. EcoCyc synonyms: mutD. Genomic coordinates: 236067-236798. EcoCyc protein note: The epsilon subunit of DNA polymerase III catalyzes the 3' to 5' proofreading exonuclease activity of the holoenzyme . This activity is required to prevent spontaneous mutations and may play a role in preventing UV mutagenesis and lesion bypass synthesis as well . The epsilon subunit suppresses both misincorporation of dCMP and transversion mutations . Episilon isrequired for speed and processivity of DNA polymerase III function . In the presence of polymerase III alpha subunit, epsilon activity increases ten- to eighty-fold, and its affinity for the 3'-hydroxy terminus of DNA increases substantially . Single-stranded DNA binding protein inhibits epsilon activity during replication...

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03007|protein.P03007]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000722,ECOCYC:EG10243,GeneID:946441`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:236067-236798:+; feature_type=gene
