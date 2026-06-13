---
entity_id: "gene.b0254"
entity_type: "gene"
name: "perR"
source_database: "NCBI RefSeq"
source_id: "gene-b0254"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0254"
  - "perR"
---

# perR

`gene.b0254`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0254`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

perR (gene.b0254) is a gene entity. It encodes perR (protein.Q57083). Encoded protein function: FUNCTION: Apparent regulatory gene involved in peroxide resistance in stationary phase. EcoCyc product frame: G6129-MONOMER. Genomic coordinates: 269289-270182. EcoCyc protein note: The PerR transcriptional regulator, which appears to belong to the LysR-family , has been widely analyzed in B. subtilis, where several DNA binding sites recognized by PerR were identified . In E. coli, the PerR protein and its binding sites has not been analyzed. But an Helix-Turn-Helix motif, that is a characteristic of transcriptional regulators, was observed in the sequence on this protein in E. coli . In systematic studies of oligomerization, it was shown that some members of the LysR family, like PerR, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . The perR knockout strain exhibits growth exclusively in a minimal medium in the presence of doxycycline, presumably due to the antioxidative properties of the antibiotic . These observations suggest the potential involvement of PerR in the cellular response to oxidative stress .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q57083|protein.Q57083]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000862,ECOCYC:G6129,GeneID:945417`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:269289-270182:-; feature_type=gene
