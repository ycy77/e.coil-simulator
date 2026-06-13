---
entity_id: "gene.b4238"
entity_type: "gene"
name: "nrdD"
source_database: "NCBI RefSeq"
source_id: "gene-b4238"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4238"
  - "nrdD"
---

# nrdD

`gene.b4238`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4238`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrdD (gene.b4238) is a gene entity. It encodes nrdD (protein.P28903). Encoded protein function: FUNCTION: Catalyzes the conversion of ribonucleotides into deoxyribonucleotides, which are required for DNA synthesis and repair (PubMed:1460049, PubMed:24827372, PubMed:7568012, PubMed:7929317, PubMed:8381402, PubMed:9305874). Can reduce each of the four common ribonucleoside triphosphates (PubMed:7929317). {ECO:0000269|PubMed:1460049, ECO:0000269|PubMed:24827372, ECO:0000269|PubMed:7568012, ECO:0000269|PubMed:7929317, ECO:0000269|PubMed:8381402, ECO:0000269|PubMed:9305874}. EcoCyc product frame: RIBONUCLEOSIDE-TRIP-REDUCT-MONOMER. Genomic coordinates: 4460522-4462660. EcoCyc protein note: Ribonucleotide reductases (RNRs) catalyze the conversion of ribonucleotides into deoxyribonucleotides, which are required for DNA synthesis and repair. Nucleotide reduction involves a transient protein-based thiyl radical that abstracts a hydrogen atom from the 2'-position of the nucleotide. Three classes of RNR enzymes have been identified; they differ in the metallocofactor required for generating the thiyl radical. E. coli contains three RNRs, the class Ia RIBONUCLEOSIDE-DIP-REDUCTI-CPLX, the class Ib RIBONUCLEOSIDE-DIP-REDUCTII-CPLX, and the class III anaerobic ribonucleoside-triphosphate reductase (NrdD) described here...

## Biological Role

Repressed by nrdR (protein.P0A8D0), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28903|protein.P28903]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrdD; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nrdD; function=+
- `represses` <-- [[protein.P0A8D0|protein.P0A8D0]] `RegulonDB` `S` - regulator=NrdR; target=nrdD; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=nrdD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013865,ECOCYC:EG11417,GeneID:948755`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4460522-4462660:-; feature_type=gene
