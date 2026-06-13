---
entity_id: "gene.b0423"
entity_type: "gene"
name: "thiI"
source_database: "NCBI RefSeq"
source_id: "gene-b0423"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0423"
  - "thiI"
---

# thiI

`gene.b0423`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0423`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiI (gene.b0423) is a gene entity. It encodes thiI (protein.P77718). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent transfer of a sulfur to tRNA to produce 4-thiouridine in position 8 of tRNAs, which functions as a near-UV photosensor. Also catalyzes the transfer of sulfur to the sulfur carrier protein ThiS, forming ThiS-thiocarboxylate. This is a step in the synthesis of thiazole, in the thiamine biosynthesis pathway. The sulfur is donated as persulfide by IscS. {ECO:0000269|PubMed:10722656, ECO:0000269|PubMed:10753862, ECO:0000269|PubMed:18604845}. EcoCyc product frame: THII-MONOMER. EcoCyc synonyms: nuvA, yajK. Genomic coordinates: 441549-442997. EcoCyc protein note: ThiI is a bifunctional enzyme that is required both for the conversion of uridine to 4-thiouridine (s4U) at position 8 in certain tRNAs and for the synthesis of the thiazole moiety of thiamine. The protien contains several functional domains - an N-terminal ferredoxin-like domain (NFLD), a THUMP (THioUridine synthases, RNA Methylases and Pseudouridine synthases) domain, a PP-loop-containing pyrophosphatase domain (the catalytic domain), and a rhodanese domain. The THUMP domain is known to specifically interact with tRNAs that are modified at position 6, 8 or 10...

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77718|protein.P77718]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001470,ECOCYC:G6238,GeneID:945067`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:441549-442997:+; feature_type=gene
