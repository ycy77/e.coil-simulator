---
entity_id: "gene.b4187"
entity_type: "gene"
name: "aidB"
source_database: "NCBI RefSeq"
source_id: "gene-b4187"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4187"
  - "aidB"
---

# aidB

`gene.b4187`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4187`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aidB (gene.b4187) is a gene entity. It encodes aidB (protein.P33224). Encoded protein function: FUNCTION: Part of the adaptive DNA-repair response to alkylating agents. Could prevent alkylation damage by protecting DNA and destroying alkylating agents that have yet to reach their DNA target. Binds to double-stranded DNA with a preference for a DNA region that includes its own promoter. Shows weak isovaleryl-CoA dehydrogenase activity in vitro. {ECO:0000269|PubMed:16352838, ECO:0000269|PubMed:18829440, ECO:0000269|PubMed:7961409}. EcoCyc product frame: EG11811-MONOMER. Genomic coordinates: 4414275-4415900. EcoCyc protein note: AidB is a multifunctional protein that forms part of E.coli's adaptive response to alkylating agents as defined by the ada regulon. The biological role of AidB is not clear - the purified protein has low levels of isovaleryl-CoA dehydrogenase activity, displays DNA binding activity and can negatively regulate its own expression in vivo. Apo AidB has a high affinity for flavin adenine dinucleotide (FAD), which helps with the assembly of the AidB tetramer . AidB was overexpressed, purified, and found to contain a FAD cofactor in stoichiometric quantities . The purified protein has a very low level of isovaleryl-CoA dehydrogenase activity and binds double-stranded DNA with a preference for methylated and/or relaxed DNA...

## Biological Role

Repressed by lrp (protein.P0ACJ0), aidB (protein.P33224). Activated by rpoD (protein.P00579), ada (protein.P06134), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33224|protein.P33224]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aidB; function=+
- `activates` <-- [[protein.P06134|protein.P06134]] `RegulonDB` `S` - regulator=Ada; target=aidB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=aidB; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=aidB; function=-
- `represses` <-- [[protein.P33224|protein.P33224]] `RegulonDB` `S` - regulator=AidB; target=aidB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013701,ECOCYC:EG11811,GeneID:948710`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4414275-4415900:+; feature_type=gene
