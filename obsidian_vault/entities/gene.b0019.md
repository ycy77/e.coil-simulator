---
entity_id: "gene.b0019"
entity_type: "gene"
name: "nhaA"
source_database: "NCBI RefSeq"
source_id: "gene-b0019"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0019"
  - "nhaA"
---

# nhaA

`gene.b0019`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0019`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nhaA (gene.b0019) is a gene entity. It encodes nhaA (protein.P13738). Encoded protein function: FUNCTION: Na(+)/H(+) antiporter that extrudes sodium in exchange for external protons (PubMed:1645730, PubMed:23836890, PubMed:2839489, PubMed:7737413, PubMed:8019504, PubMed:8383669). Plays an important role in the regulation of intracellular pH, cellular Na(+) content and cell volume (PubMed:33129932). Catalyzes the exchange of 2 H(+) per Na(+) (PubMed:23836890, PubMed:8383669). This stoichiometry applies at both neutral and alkaline pH values (PubMed:8383669). In addition, can also transport lithium and is involved in lithium detoxification (PubMed:22915592, PubMed:27021484, PubMed:7737413, PubMed:8019504). Binding of the Li(+) and H(+) ligands to NhaA is coupled and antagonistic (PubMed:27021484). {ECO:0000269|PubMed:1645730, ECO:0000269|PubMed:22915592, ECO:0000269|PubMed:23836890, ECO:0000269|PubMed:27021484, ECO:0000269|PubMed:2839489, ECO:0000269|PubMed:7737413, ECO:0000269|PubMed:8019504, ECO:0000269|PubMed:8383669, ECO:0000303|PubMed:33129932}. EcoCyc product frame: NHAA-MONOMER. EcoCyc synonyms: ant, antA. Genomic coordinates: 17489-18655. EcoCyc protein note: NhaA is an Na+:H+ antiporter with a prominent role in sodium ion and alkaline pH homeostasis...

## Biological Role

Activated by rpoD (protein.P00579), nhaR (protein.P0A9G2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13738|protein.P13738]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nhaA; function=+
- `activates` <-- [[protein.P0A9G2|protein.P0A9G2]] `RegulonDB` `S` - regulator=NhaR; target=nhaA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000068,ECOCYC:EG10652,GeneID:944758`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:17489-18655:+; feature_type=gene
