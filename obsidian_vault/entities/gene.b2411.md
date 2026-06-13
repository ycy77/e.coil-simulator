---
entity_id: "gene.b2411"
entity_type: "gene"
name: "ligA"
source_database: "NCBI RefSeq"
source_id: "gene-b2411"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2411"
  - "ligA"
---

# ligA

`gene.b2411`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2411`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ligA (gene.b2411) is a gene entity. It encodes ligA (protein.P15042). Encoded protein function: FUNCTION: DNA ligase that catalyzes the formation of phosphodiester linkages between 5'-phosphoryl and 3'-hydroxyl groups in double-stranded DNA using NAD as a coenzyme and as the energy source for the reaction. It is essential for DNA replication and repair of damaged DNA. EcoCyc product frame: EG10534-MONOMER. EcoCyc synonyms: dnaL, lig, lop, pdeC. Genomic coordinates: 2528161-2530176. EcoCyc protein note: LigA is one of two known NAD(+)-dependent DNA ligases, catalyzing the formation of phosphodiester bonds in duplex DNA. LigA ligates duplex DNA in an NAD(+)-dependent fashion . Kinetic evaluations have yielded differing kM values for NAD(+) ranging from 0.7 to 7 μM, a kM for strand breaks of 0.03-0.06 μM and a turnover number of 25 ligations per minute . Participation of fluorescently labeled LigA in the repair of single nucleotide gaps generated during base excision repair (BER) in live E. coli cells has been visualised and quantified . The ligation reaction proceeds via three steps and involves two intermediates - an enzyme-adenylate complex and a DNA adenylate complex . In the absence of DNA, purified E. coli ligase reacts with NAD and forms a stable enzyme-adenylate complex releasing nicotinamide mononucleotide (NMN)...

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03410` Base excision repair (KEGG)
- `eco03420` Nucleotide excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15042|protein.P15042]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007938,ECOCYC:EG10534,GeneID:946885`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2528161-2530176:-; feature_type=gene
