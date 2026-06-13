---
entity_id: "protein.P24255"
entity_type: "protein"
name: "rpoN"
source_database: "UniProt"
source_id: "P24255"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpoN glnF ntrA b3202 JW3169"
---

# rpoN

`protein.P24255`

## Static

- Type: `protein`
- Source: `UniProt:P24255`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor is responsible for the expression of enzymes involved in arginine catabolism. The open complex (sigma-54 and core RNA polymerase) serves as the receptor for the receipt of the melting signal from the remotely bound activator protein GlnG(NtrC). Sigma 54 controls expression of nitrogen-related genes, directing RNAP54-CPLX to the consensus nitrogen promoter. Sigma 54 is the sigma factor controlling nitrogen-regulated and other nitrogen-related promoters . It copurifies with the RNA polymerase core enzyme and binds to the consensus nitrogen promoter . It is also involved in the nitric oxide stress response . Mutants lacking rpoN had a significant defect in polyP synthesis . During typical exponential and stationary phase growth, the amount of sigma 54 present in the cell is one tenth that of the amount of sigma 70 . The metabolic context of genes dependent on sigma54 for transcription is reviewed in . The alternative sigma factor σ54 (RpoN or σN) requires activation by specialized AAA+ ATPases (bacterial enhancer-binding proteins, bEBPs) such as the NtrC protein...

## Biological Role

Component of RNA polymerase sigma 54 (complex.ecocyc.RNAP54-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor is responsible for the expression of enzymes involved in arginine catabolism. The open complex (sigma-54 and core RNA polymerase) serves as the receptor for the receipt of the melting signal from the remotely bound activator protein GlnG(NtrC).

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (53)

- `activates` --> [[gene.b1744|gene.b1744]] `RegulonDB` `C` - sigma=sigma54; target=astE; function=+
- `activates` --> [[gene.b1745|gene.b1745]] `RegulonDB` `C` - sigma=sigma54; target=astB; function=+
- `activates` --> [[gene.b1746|gene.b1746]] `RegulonDB` `C` - sigma=sigma54; target=astD; function=+
- `activates` --> [[gene.b1747|gene.b1747]] `RegulonDB` `C` - sigma=sigma54; target=astA; function=+
- `activates` --> [[gene.b1748|gene.b1748]] `RegulonDB` `C` - sigma=sigma54; target=astC; function=+
- `activates` --> [[gene.b1988|gene.b1988]] `RegulonDB` `S` - sigma=sigma54; target=nac; function=+
- `activates` --> [[gene.b2239|gene.b2239]] `RegulonDB` `S` - sigma=sigma54; target=glpQ; function=+
- `activates` --> [[gene.b2406|gene.b2406]] `RegulonDB` `S` - sigma=sigma54; target=xapB; function=+
- `activates` --> [[gene.b2570|gene.b2570]] `RegulonDB` `S` - sigma=sigma54; target=rseC; function=+
- `activates` --> [[gene.b2571|gene.b2571]] `RegulonDB` `S` - sigma=sigma54; target=rseB; function=+
- `activates` --> [[gene.b2572|gene.b2572]] `RegulonDB` `S` - sigma=sigma54; target=rseA; function=+
- `activates` --> [[gene.b2573|gene.b2573]] `RegulonDB` `S` - sigma=sigma54; target=rpoE; function=+
- `activates` --> [[gene.b2710|gene.b2710]] `RegulonDB` `S` - sigma=sigma54; target=norV; function=+
- `activates` --> [[gene.b2711|gene.b2711]] `RegulonDB` `S` - sigma=sigma54; target=norW; function=+
- `activates` --> [[gene.b2717|gene.b2717]] `RegulonDB` `S` - sigma=sigma54; target=hycI; function=+
- `activates` --> [[gene.b2718|gene.b2718]] `RegulonDB` `S` - sigma=sigma54; target=hycH; function=+
- `activates` --> [[gene.b2719|gene.b2719]] `RegulonDB` `S` - sigma=sigma54; target=hycG; function=+
- `activates` --> [[gene.b2720|gene.b2720]] `RegulonDB` `S` - sigma=sigma54; target=hycF; function=+
- `activates` --> [[gene.b2721|gene.b2721]] `RegulonDB` `S` - sigma=sigma54; target=hycE; function=+
- `activates` --> [[gene.b2722|gene.b2722]] `RegulonDB` `S` - sigma=sigma54; target=hycD; function=+
- `activates` --> [[gene.b2723|gene.b2723]] `RegulonDB` `S` - sigma=sigma54; target=hycC; function=+
- `activates` --> [[gene.b2724|gene.b2724]] `RegulonDB` `S` - sigma=sigma54; target=hycB; function=+
- `activates` --> [[gene.b2725|gene.b2725]] `RegulonDB` `S` - sigma=sigma54; target=hycA; function=+
- `activates` --> [[gene.b2726|gene.b2726]] `RegulonDB` `S` - sigma=sigma54; target=hypA; function=+
- `activates` --> [[gene.b2727|gene.b2727]] `RegulonDB` `S` - sigma=sigma54; target=hypB; function=+
- `activates` --> [[gene.b2728|gene.b2728]] `RegulonDB` `S` - sigma=sigma54; target=hypC; function=+
- `activates` --> [[gene.b2729|gene.b2729]] `RegulonDB` `S` - sigma=sigma54; target=hypD; function=+
- `activates` --> [[gene.b2730|gene.b2730]] `RegulonDB` `S` - sigma=sigma54; target=hypE; function=+
- `activates` --> [[gene.b2731|gene.b2731]] `RegulonDB` `S` - sigma=sigma54; target=fhlA; function=+
- `activates` --> [[gene.b2784|gene.b2784]] `RegulonDB` `S` - sigma=sigma54; target=relA; function=+
- `activates` --> [[gene.b2866|gene.b2866]] `RegulonDB` `S` - sigma=sigma54; target=xdhA; function=+
- `activates` --> [[gene.b2867|gene.b2867]] `RegulonDB` `S` - sigma=sigma54; target=xdhB; function=+
- `activates` --> [[gene.b2868|gene.b2868]] `RegulonDB` `S` - sigma=sigma54; target=xdhC; function=+
- `activates` --> [[gene.b3073|gene.b3073]] `RegulonDB` `S` - sigma=sigma54; target=patA; function=+
- `activates` --> [[gene.b3421|gene.b3421]] `RegulonDB` `S` - sigma=sigma54; target=rtcB; function=+
- `activates` --> [[gene.b3461|gene.b3461]] `RegulonDB` `C` - sigma=sigma54; target=rpoH; function=+
- `activates` --> [[gene.b3868|gene.b3868]] `RegulonDB` `S` - sigma=sigma54; target=glnG; function=+
- `activates` --> [[gene.b3869|gene.b3869]] `RegulonDB` `S` - sigma=sigma54; target=glnL; function=+
- `activates` --> [[gene.b3870|gene.b3870]] `RegulonDB` `S` - sigma=sigma54; target=glnA; function=+
- `activates` --> [[gene.b4050|gene.b4050]] `RegulonDB` `S` - sigma=sigma54; target=pspG; function=+
- `activates` --> [[gene.b4441|gene.b4441]] `RegulonDB` `S` - sigma=sigma54; target=glmY; function=+
- `activates` --> [[gene.b4475|gene.b4475]] `RegulonDB` `S` - sigma=sigma54; target=rtcA; function=+
- `activates` --> [[gene.b4517|gene.b4517]] `RegulonDB` `S` - sigma=sigma54; target=gnsA; function=+
- `activates` --> [[gene.b4725|gene.b4725]] `RegulonDB` `S` - sigma=sigma54; target=rseD; function=+
- `activates` --> [[gene.b4758|gene.b4758]] `RegulonDB` `S` - sigma=sigma54; target=pspH; function=+
- `activates` --> [[gene.b4836|gene.b4836]] `RegulonDB` `S` - sigma=sigma54; target=glnZ; function=+
- `is_component_of` --> [[complex.ecocyc.RNAP54-CPLX|complex.ecocyc.RNAP54-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `represses` --> [[gene.b1633|gene.b1633]] `RegulonDB|EcoCyc` `S` - regulator=RpoN; target=nth; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1823|gene.b1823]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1824|gene.b1824]] `RegulonDB|EcoCyc` `S` - regulator=RpoN; target=yobF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2343|gene.b2343]] `RegulonDB|EcoCyc` `S` - regulator=RpoN; target=yfcZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2344|gene.b2344]] `RegulonDB|EcoCyc` `S` - regulator=RpoN; target=fadL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3635|gene.b3635]] `RegulonDB|EcoCyc` `S` - regulator=RpoN; target=mutM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b3202|gene.b3202]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24255`
- `KEGG:ecj:JW3169;eco:b3202;ecoc:C3026_17425;`
- `GeneID:947714;`
- `GO:GO:0000345; GO:0000976; GO:0001216; GO:0006352; GO:0006355; GO:0006525; GO:0016779; GO:0016987; GO:0032993; GO:0042128; GO:0045893; GO:0048870; GO:0090605; GO:2000142`

## Notes

RNA polymerase sigma-54 factor
