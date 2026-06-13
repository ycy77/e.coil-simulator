---
entity_id: "gene.b3942"
entity_type: "gene"
name: "katG"
source_database: "NCBI RefSeq"
source_id: "gene-b3942"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3942"
  - "katG"
---

# katG

`gene.b3942`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3942`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

katG (gene.b3942) is a gene entity. It encodes katG (protein.P13029). Encoded protein function: FUNCTION: Bifunctional enzyme with both catalase and broad-spectrum peroxidase activity. Also displays NADH oxidase, INH lyase and isonicotinoyl-NAD synthase activities. {ECO:0000269|PubMed:18178143, ECO:0000269|PubMed:23416055, ECO:0000269|PubMed:374409}. EcoCyc product frame: HYDROPEROXIDI-MONOMER. Genomic coordinates: 4133835-4136015. EcoCyc protein note: There are two distinct catalases in E. coli. The KatG enzyme is the bifunctional hydroperoxidase I (HPI), with both catalase and peroxidase activity. A monofunctional catalase, HPII, is encoded by katE . Endogenously produced H2O2 is primarily scavenged by a third enzyme, CPLX0-245, while catalase is the primary scavenger at high H2O2 concentrations . The catalase activity uses one molecule of H2O2 as the electron donor and a second molecule of H2O2 as the electron acceptor, producing oxygen and water. At lower concentrations of H2O2, the peroxidase activity is able to utilize a suitable electron donor other than H2O2 . For both activities, the initial step is the reduction of H2O2 to H2O by a ferric heme, producing the ferryl porphyrin cation radical intermediate known as compound I. In the catalase reaction, compound I is returned directly to the ferric state by oxidizing a second molecule of H2O2 to O2...

## Biological Role

Repressed by sdhX (gene.b4764), nac (protein.Q47005). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), rpoD (protein.P00579), fnr (protein.P0A9E5), oxyR (protein.P0ACQ4).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13029|protein.P13029]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=katG; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=katG; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=katG; function=+
- `represses` <-- [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=SdhX; target=katG; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=katG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012901,ECOCYC:EG10511,GeneID:948431`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4133835-4136015:+; feature_type=gene
