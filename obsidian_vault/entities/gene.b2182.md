---
entity_id: "gene.b2182"
entity_type: "gene"
name: "bcr"
source_database: "NCBI RefSeq"
source_id: "gene-b2182"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2182"
  - "bcr"
---

# bcr

`gene.b2182`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2182`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bcr (gene.b2182) is a gene entity. It encodes bcr (protein.P28246). Encoded protein function: FUNCTION: Involved in sulfonamide (sulfathiazole) and bicyclomycin resistance (PubMed:2694948). Probable membrane translocase. A transporter able to export peptides. When overexpressed, allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide overproduction of this protein increases export of the dipeptide (PubMed:20067529). {ECO:0000269|PubMed:2694948}. EcoCyc product frame: BCR-MONOMER. EcoCyc synonyms: bicA, bicR, sur, suxA. Genomic coordinates: 2278570-2279760. EcoCyc protein note: Expression of bcr from a high-copy number plasmid confers resistance to the antibiotic bicyclomycin ; increased expression of bcr contributes to sulfathiazole resistance in an E. coli strain that also contains a sulfathiazole-resistant H2PTEROATESYNTH-MONOMER . Multicopy expression of bcr in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ), confers moderate resistance to tetracycline, fosfomycin, kanamycin and acriflavine but does not impact the resistance to a range of other antibiotics and toxic compounds...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28246|protein.P28246]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007221,ECOCYC:EG11419,GeneID:944808`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2278570-2279760:-; feature_type=gene
