---
entity_id: "gene.b3633"
entity_type: "gene"
name: "waaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3633"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3633"
  - "waaA"
---

# waaA

`gene.b3633`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3633`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaA (gene.b3633) is a gene entity. It encodes waaA (protein.P0AC75). Encoded protein function: FUNCTION: Involved in lipopolysaccharide (LPS) biosynthesis. Catalyzes the transfer of two 3-deoxy-D-manno-octulosonate (Kdo) residues from CMP-Kdo to lipid IV(A), the tetraacyldisaccharide-1,4'-bisphosphate precursor of lipid A. {ECO:0000269|PubMed:10951204, ECO:0000269|PubMed:1577828}. EcoCyc product frame: KDOTRANS-MONOMER. EcoCyc synonyms: kdtA. Genomic coordinates: 3808540-3809817. EcoCyc protein note: 3-deoxy-D-manno-octulosonic acid (KDO) transferase (KdtA, WaaA) plays a key role in lipopolysaccharide biosynthesis. The enzyme is a single bifunctional polypeptide that incorporates the two innermost KDO residues into lipid IVA, the lipid A precursor. The KDO residues are transferred in two sequential steps . KDO transferase is an integral membrane protein . The N-terminal domain of WaaA determines the bifunctionality of E.coli WaaA which is in contrast to the KDO transferase of Haemophilus influenzae which adds only one KDO residue to Lipid A . KDO transferase is encoded by kdta (waaA) which has been sequenced, cloned and the gene product overexpressed . Deletion of kdtA resulted in highly attenuated growth, accumulation of free lipid IVA precursors, constitutively elevated levels of periplasmic protease HtrA, and severe membrane and cell division defects...

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC75|protein.P0AC75]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=waaA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=waaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011873,ECOCYC:EG10520,GeneID:949048`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3808540-3809817:+; feature_type=gene
