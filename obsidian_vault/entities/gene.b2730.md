---
entity_id: "gene.b2730"
entity_type: "gene"
name: "hypE"
source_database: "NCBI RefSeq"
source_id: "gene-b2730"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2730"
  - "hypE"
---

# hypE

`gene.b2730`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2730`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hypE (gene.b2730) is a gene entity. It encodes hypE (protein.P24193). Encoded protein function: FUNCTION: Involved in the maturation of [NiFe] hydrogenases. Along with HypF, it catalyzes the synthesis of the CN ligands of the active site iron of [NiFe]-hydrogenases. HypE catalyzes the ATP-dependent dehydration of the carboxamido group attached to its C-terminal cysteine to a cyano group (PubMed:12586941, PubMed:15291820). The cyano group is then transferred from HypE to the HypC-HypD complex or the HybG-HypD complex (PubMed:15504408). {ECO:0000269|PubMed:12586941, ECO:0000269|PubMed:15291820, ECO:0000269|PubMed:15504408}. EcoCyc product frame: MONOMER0-4166. EcoCyc synonyms: hydB. Genomic coordinates: 2853254-2854264. EcoCyc protein note: HypE is one of the hydrogenase maturation proteins required for the assembly of the CN ligand of the NiFe metal center of FORMHYDROGI-CPLX, FORMHYDROG2-CPLX and HYDROG3-CPLX. At least seven gene products are involved in the maturation of hydrogenases, which includes the generation and incorporation of the CN ligand from carbamoylphosphate (CP). First, EG11551-MONOMER HypF converts CP and ATP to carbamoyladenylate, inorganic phosphate, pyrophosphate, and AMP . It then transfers the carbamoyl group to the carboxy terminal cysteine of HypE...

## Biological Role

Activated by fnr (protein.P0A9E5), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24193|protein.P24193]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=hypE; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hypE; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hypE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008967,ECOCYC:EG10487,GeneID:947182`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2853254-2854264:+; feature_type=gene
