---
entity_id: "gene.b0573"
entity_type: "gene"
name: "cusF"
source_database: "NCBI RefSeq"
source_id: "gene-b0573"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0573"
  - "cusF"
---

# cusF

`gene.b0573`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0573`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cusF (gene.b0573) is a gene entity. It encodes cusF (protein.P77214). Encoded protein function: FUNCTION: Part of a cation efflux system that mediates resistance to copper and silver. Binds one copper per polypeptide (PubMed:11399769, PubMed:24917681). {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:24917681}. EcoCyc product frame: G6321-MONOMER. EcoCyc synonyms: cusX, ylcC. Genomic coordinates: 597131-597463. EcoCyc protein note: CusF is a periplasmic binding protein involved in the detoxification of copper and silver ions in E. coli as part of the CusCFBA copper/silver efflux system. CusF forms a five-stranded β-barrel and has been crystallized in its apo form as well as with bound Ag(I) or Cu(I) . CusF is a metallochaperone that specifically binds Ag(I) and Cu(I), but not Cu(II) despite earlier evidence regarding binding of Cu(II) . CusF transfers metal directly to CusB for export . CusF is a pink copper-binding protein and binds one copper ion per monomer . The histidine residue at position 58 and the two methionine residues at positions 69 and 71 are essential for copper/silver binding . Cu(I) binding also involves a strong interaction between the metal ion and the aromatic ring of a tryptophan residue at position 44 . The Trp-44 'capping ligand' serves a protective function, preventing access of oxygen to the Cu(I) center...

## Biological Role

Repressed by yciT (protein.P76034). Activated by rpoD (protein.P00579), cusR (protein.P0ACZ8), phoB (protein.P0AFJ5), hprR (protein.P76340).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77214|protein.P77214]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cusF; function=+
- `activates` <-- [[protein.P0ACZ8|protein.P0ACZ8]] `RegulonDB` `C` - regulator=CusR; target=cusF; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=cusF; function=+
- `activates` <-- [[protein.P76340|protein.P76340]] `RegulonDB` `S` - regulator=HprR; target=cusF; function=+
- `represses` <-- [[protein.P76034|protein.P76034]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001967,ECOCYC:G6321,GeneID:945188`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:597131-597463:+; feature_type=gene
