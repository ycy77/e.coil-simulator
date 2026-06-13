---
entity_id: "gene.b4003"
entity_type: "gene"
name: "zraS"
source_database: "NCBI RefSeq"
source_id: "gene-b4003"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4003"
  - "zraS"
---

# zraS

`gene.b4003`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4003`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zraS (gene.b4003) is a gene entity. It encodes zraS (protein.P14377). Encoded protein function: FUNCTION: Part of the Zra signaling pathway, an envelope stress response (ESR) system composed of the periplasmic accessory protein ZraP, the histidine kinase ZraS and the transcriptional regulator ZraR (PubMed:26438879, PubMed:30389436, PubMed:33309686). The ZraPSR system contributes to antibiotic resistance and is important for membrane integrity in the presence of membrane-targeting biocides (PubMed:30389436). ZraS is a member of the two-component regulatory system ZraS/ZraR (PubMed:11243806). Functions as a membrane-associated sensor kinase that phosphorylates ZraR in response to high concentrations of Zn(2+) or Pb(2+) in the medium (PubMed:11243806, PubMed:15522865). Binds one zinc molecule with high affinity via its periplasmic domain, inducing a conformational change that is transmitted to the histidine kinase domain and leads to the activation of ZraR (PubMed:33309686). The system has no direct role in zinc or copper resistance (PubMed:26438879). {ECO:0000269|PubMed:11243806, ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:26438879, ECO:0000269|PubMed:30389436, ECO:0000269|PubMed:33309686}. EcoCyc product frame: PHOSPHO-HYDH. EcoCyc synonyms: hydH. Genomic coordinates: 4201926-4203323...

## Biological Role

Activated by zraR (protein.P14375).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P14377|protein.P14377]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB` `S` - regulator=ZraR; target=zraS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013088,ECOCYC:EG10008,GeneID:948506`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4201926-4203323:+; feature_type=gene
