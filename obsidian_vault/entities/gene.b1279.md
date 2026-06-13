---
entity_id: "gene.b1279"
entity_type: "gene"
name: "lapA"
source_database: "NCBI RefSeq"
source_id: "gene-b1279"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1279"
  - "lapA"
---

# lapA

`gene.b1279`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1279`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lapA (gene.b1279) is a gene entity. It encodes lapA (protein.P0ACV4). Encoded protein function: FUNCTION: Involved in the assembly of lipopolysaccharide (LPS). {ECO:0000255|HAMAP-Rule:MF_01948, ECO:0000269|PubMed:24722986}. EcoCyc product frame: G6637-MONOMER. EcoCyc synonyms: yciS. Genomic coordinates: 1340243-1340551. EcoCyc protein note: lapA is generally not essential. ΔlapA strains do not grow on MacConkey agar at 43°C. LapA copurifies with LapB, DnaK, DnaJ and with the LPS transport system proteins (LptE/D, LptBFGC, LptA). Purified LapA contains lipopolysaccharide (LPS) . lapAB transcription is subject to heat shock induction via an RpoH-regulated promoter located upstream of lapA . LapA is an inner membrane protein with two predicted transmembrane domains. The C terminus is located in the cytoplasm . LapA was identified in a phylogenetic screen that found proteins containing domains that only occur in organisms that also contain a EG10204-MONOMER Dam methyltransferase . LapA: lipopolysaccharide assembly protein A

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACV4|protein.P0ACV4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lapA; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=lapA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004298,ECOCYC:G6637,GeneID:944936`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1340243-1340551:+; feature_type=gene
