---
entity_id: "gene.b1732"
entity_type: "gene"
name: "katE"
source_database: "NCBI RefSeq"
source_id: "gene-b1732"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1732"
  - "katE"
---

# katE

`gene.b1732`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1732`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

katE (gene.b1732) is a gene entity. It encodes katE (protein.P21179). Encoded protein function: FUNCTION: Decomposes hydrogen peroxide into water and oxygen; serves to protect cells from the toxic effects of hydrogen peroxide. EcoCyc product frame: HYDROPEROXIDII-MONOMER. Genomic coordinates: 1813867-1816128. EcoCyc protein note: There are two distinct catalases in E. coli. The KatE enzyme is the monofunctional catalase HPII. A bifunctional catalase, HPI, is encoded by katG . Aerobically grown E. coli produce sufficient endogenous H2O2 to cause toxic levels of DNA damage via the Fenton reaction ; endogenously produced H2O2 is primarily scavenged by a third enzyme, CPLX0-245, while catalase is the primary scavenger at high H2O2 concentrations . While most heme proteins contain PROTOHEME as the prosthetic group, HPII contains a unique cofactor, HEME_D. It has been suggested that heme d is formed in a reaction catalyzed by HPII itself. Based on this model, HPII first binds protoheme, which is subsequently hydroxylated by HPII utilizing one of the first H2O2 substrate molecules . Later work has supported this theory. While HPII from aerobically grown E. coli contains heme d, HPII purified from microaerobic or anaerobic cultures contains a mixture of heme d and PROTOHEME...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0), rpoS (protein.P13445).

## Enriched Pathways

- `eco00380` Tryptophan metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco04146` Peroxisome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21179|protein.P21179]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=katE; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005780,ECOCYC:EG10509,GeneID:946234`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1813867-1816128:+; feature_type=gene
