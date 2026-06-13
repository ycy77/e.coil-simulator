---
entity_id: "gene.b0622"
entity_type: "gene"
name: "pagP"
source_database: "NCBI RefSeq"
source_id: "gene-b0622"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0622"
  - "pagP"
---

# pagP

`gene.b0622`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0622`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pagP (gene.b0622) is a gene entity. It encodes pagP (protein.P37001). Encoded protein function: FUNCTION: Transfers a palmitate residue from the sn-1 position of a phospholipid to the N-linked hydroxymyristate on the proximal unit of lipid A or its precursors. Phosphatidylglycerol (PtdGro), phosphatidylethanolamine (PtdEtn), phosphatidylserine (PtdSer) and phosphatidic acid (Ptd-OH) are all effective acyl donors. {ECO:0000269|PubMed:11013210, ECO:0000269|PubMed:20826347, ECO:0000269|PubMed:20853818}. EcoCyc product frame: EG12180-MONOMER. EcoCyc synonyms: ybeG, crcA. Genomic coordinates: 656557-657117. EcoCyc protein note: The outer membrane protein PagP catalyses the transfer of a palmitate chain from phospholipid donor to the lipid A moiety of lipopolysaccharide (LPS), a modification that is important for virulence in many gram-negative bacteria. Purified PagP transfers a palmitate chain from the sn-1 position of a phospholipid substrate (phosphatidylcholine substrates and common E. coli phospholipids) to the amide-linked hydroxymyristate chain of the proximal glucosamine unit (GlcN I) of disaccharide lipid A precursors (lipid IVA and Kdo2-lipid IVA) in vitro; the expected physiological substrate of PagP is the lipid A moiety of fully assembled CPD0-939 "LPS" in the outer membrane; PagP is highly selective for a saturated palmitate chain...

## Biological Role

Repressed by hns (protein.P0ACF8).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37001|protein.P37001]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002139,ECOCYC:EG12180,GeneID:946360`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:656557-657117:+; feature_type=gene
