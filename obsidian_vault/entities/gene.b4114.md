---
entity_id: "gene.b4114"
entity_type: "gene"
name: "eptA"
source_database: "NCBI RefSeq"
source_id: "gene-b4114"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4114"
  - "eptA"
---

# eptA

`gene.b4114`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4114`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eptA (gene.b4114) is a gene entity. It encodes eptA (protein.P30845). Encoded protein function: FUNCTION: Catalyzes the addition of a phosphoethanolamine moiety to the lipid A. The phosphoethanolamine modification is required for resistance to polymyxin. {ECO:0000250|UniProtKB:A0A0H3JML2}. EcoCyc product frame: EG11613-MONOMER. EcoCyc synonyms: yjdB. Genomic coordinates: 4333947-4335590. EcoCyc protein note: EptA catalyses the addition of PHOSPHORYL-ETHANOLAMINE (pEtN) to the glucosamine disaccharide of lipid A core oligosaccharide. This modification promotes resistance to Polymyxins "polymyxin antibiotics" and antimicrobial peptides. L-1-PHOSPHATIDYL-ETHANOLAMINE Phosphatidylethanolamine serves as the donor and transfer occurs to the 1-phosphate and/or 4'-phosphate position; the reaction occurs on the outer surface of the inner membrane . A side product of the reaction is DIACYLGLYCEROL "1,2-diacyl-sn-glycerol" (DAG), a potential inhibitor of EptA . However, the DAG that is produced in converted rapidly to L-PHOSPHATIDATE phosphatidate by DIACYLGLYKIN-CPLX . Modification of E. coli LPS with pEtN is induced in cells grown under mild acidic conditions and in cells grown in LB with ammonium metavanadate (NH4VO3)...

## Biological Role

Repressed by nac (protein.Q47005). Activated by basR (protein.P30843).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30845|protein.P30845]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `C` - regulator=BasR; target=eptA; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=eptA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013469,ECOCYC:EG11613,GeneID:948629`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4333947-4335590:-; feature_type=gene
