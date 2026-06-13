---
entity_id: "gene.b1798"
entity_type: "gene"
name: "leuE"
source_database: "NCBI RefSeq"
source_id: "gene-b1798"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1798"
  - "leuE"
---

# leuE

`gene.b1798`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1798`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuE (gene.b1798) is a gene entity. It encodes leuE (protein.P76249). Encoded protein function: FUNCTION: Exporter of leucine. Can also transport its natural analog L-alpha-amino-n-butyric acid and some other structurally unrelated amino acids. Leucine excretion is probably driven by proton motive force. {ECO:0000269|PubMed:16098526}. EcoCyc product frame: G6984-MONOMER. EcoCyc synonyms: yeaS. Genomic coordinates: 1880121-1880759. EcoCyc protein note: The leucine exporter LeuE belongs to the RhtB family of transporters. Overexpression of LeuE resulted in resistance of cells to leucine analogues, glycyl-L-leucine, and several other amino acids and their analogues. Expression of leuE was shown to be induced by leucine, L-α-amino-N-butyric acid, and several other amino acids . Leucine accumulation in a leucine-producing, leuE-overexpressing strain dropped upon addition of CCCP, revealing the dependence of transport upon the proton-motive-force . The global regulator Lrp regulates leuE expression . LeuE: "leucine export"

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76249|protein.P76249]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=leuE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005984,ECOCYC:G6984,GeneID:946157`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1880121-1880759:-; feature_type=gene
