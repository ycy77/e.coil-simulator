---
entity_id: "protein.P0A6X3"
entity_type: "protein"
name: "hfq"
source_database: "UniProt"
source_id: "P0A6X3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:36577380}. Note=Localizes along a helical path in unstressed cells and relocates to the cell poles under certain stress conditions such as osmotic stress and nutrient deprivation (PubMed:36577380). Forms cytoplasmic or polar condensates under normal or stress conditions, respectively (PubMed:36577380). Localization to the cell poles and formation of the condensates depend on the pole-localizer protein TmaR (PubMed:36577380). RNA molecules also contribute to Hfq condensate formation (PubMed:36577380). {ECO:0000269|PubMed:36577380}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hfq b4172 JW4130"
---

# hfq

`protein.P0A6X3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6X3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:36577380}. Note=Localizes along a helical path in unstressed cells and relocates to the cell poles under certain stress conditions such as osmotic stress and nutrient deprivation (PubMed:36577380). Forms cytoplasmic or polar condensates under normal or stress conditions, respectively (PubMed:36577380). Localization to the cell poles and formation of the condensates depend on the pole-localizer protein TmaR (PubMed:36577380). RNA molecules also contribute to Hfq condensate formation (PubMed:36577380). {ECO:0000269|PubMed:36577380}.

## Enriched Summary

FUNCTION: RNA chaperone that binds small regulatory RNA (sRNAs) and mRNAs to facilitate mRNA translational regulation in response to envelope stress, environmental stress and changes in metabolite concentrations. Involved in the regulation of stress responses mediated by the sigma factors RpoS, sigma-E and sigma-32 (PubMed:17158661). Binds with high specificity to tRNAs (PubMed:18230766). Binds sRNA antitoxin RalA (PubMed:24748661). In vitro, stimulates synthesis of long tails by poly(A) polymerase I (PubMed:10677490). Required for RNA phage Qbeta replication (PubMed:805130). Seems to play a role in persister cell formation; upon overexpression decreases persister cell formation while deletion increases persister formation (PubMed:19909729). {ECO:0000269|PubMed:10677490, ECO:0000269|PubMed:17158661, ECO:0000269|PubMed:18230766, ECO:0000269|PubMed:19909729, ECO:0000269|PubMed:24748661, ECO:0000269|PubMed:805130}. Hfq is an RNA chaperone and major global regulator of cell physiology. The E. coli K-12 Hfq was discovered as a host factor (HF-I) required for wild-type bacteriophage Q beta (Qβ) replication . It is structurally and functionally similar to eukaryotic Sm/Sm-like proteins with its donut-shaped, homohexamer structure and conserved core region...

## Biological Role

Component of Hfq (complex.ecocyc.CPLX0-1461).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: RNA chaperone that binds small regulatory RNA (sRNAs) and mRNAs to facilitate mRNA translational regulation in response to envelope stress, environmental stress and changes in metabolite concentrations. Involved in the regulation of stress responses mediated by the sigma factors RpoS, sigma-E and sigma-32 (PubMed:17158661). Binds with high specificity to tRNAs (PubMed:18230766). Binds sRNA antitoxin RalA (PubMed:24748661). In vitro, stimulates synthesis of long tails by poly(A) polymerase I (PubMed:10677490). Required for RNA phage Qbeta replication (PubMed:805130). Seems to play a role in persister cell formation; upon overexpression decreases persister cell formation while deletion increases persister formation (PubMed:19909729). {ECO:0000269|PubMed:10677490, ECO:0000269|PubMed:17158661, ECO:0000269|PubMed:18230766, ECO:0000269|PubMed:19909729, ECO:0000269|PubMed:24748661, ECO:0000269|PubMed:805130}.

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (6)

- `activates` --> [[gene.b3203|gene.b3203]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `is_component_of` --> [[complex.ecocyc.CPLX0-1461|complex.ecocyc.CPLX0-1461]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `represses` --> [[gene.b1817|gene.b1817]] `RegulonDB|EcoCyc` `C` - regulator=Hfq; target=manX; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b2155|gene.b2155]] `RegulonDB` `S` - regulator=Hfq; target=cirA; function=-
- `represses` --> [[gene.b2733|gene.b2733]] `RegulonDB` `S` - regulator=Hfq; target=mutS; function=-
- `represses` --> [[gene.b3204|gene.b3204]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4172|gene.b4172]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6X3`
- `KEGG:ecj:JW4130;eco:b4172;ecoc:C3026_22545;`
- `GeneID:86861434;93777649;948689;`
- `GO:GO:0000049; GO:0003677; GO:0003681; GO:0003723; GO:0005524; GO:0005829; GO:0006355; GO:0008033; GO:0040033; GO:0043487; GO:0043590; GO:0045974; GO:0045975; GO:0140691`

## Notes

RNA-binding protein Hfq (HF-1) (Host factor-I protein) (HF-I)
