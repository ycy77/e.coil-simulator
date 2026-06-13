---
entity_id: "protein.P0ACL9"
entity_type: "protein"
name: "pdhR"
source_database: "UniProt"
source_id: "P0ACL9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdhR aceC genA yacB b0113 JW0109"
---

# pdhR

`protein.P0ACL9`

## Static

- Type: `protein`
- Source: `UniProt:P0ACL9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional repressor for the pyruvate dehydrogenase complex genes aceEF and lpd. PdhR, "pyruvate dehydrogenase complex regulator," regulates genes involved in the pyruvate dehydrogenase complex . Moreover, PdhR participates in positive regulation of fatty acid degradation genes and negative regulation of cell mobility genes. Gas chromatography analysis indicated an increase in free fatty acids in a mutant lacking PdhR . PdhR controls the synthesis of two key enzymes (Ndh and CyoA) in the terminal electron transport system , the enzymes for producing pyruvate and the enzymes involved in the utilization of pyruvate as a substrate . The pdhR deletion mutant enhanced glucose metabolism under oxygen-limited conditions. This mutant strain showed increased activity of the pyruvate dehydrogenase complex and NADH dehydrogenase . Inhibition of pdhR expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic puromycin . Activity of PdhR is controlled by pyruvate. In the absence of this compound, the PdhR regulator binds to its target promoters . This binding is antagonized by pyruvate . PdhR activates a set of genes for fatty acid degradation only in the absence of effector pyruvate. Likewise, RpoF-regulated synthesis of flagellar components is also controlled by the pyruvate-sensing PdhR...

## Biological Role

Component of PdhR-pyruvate (complex.ecocyc.MONOMER-59).

## Annotation

FUNCTION: Transcriptional repressor for the pyruvate dehydrogenase complex genes aceEF and lpd.

## Outgoing Edges (47)

- `activates` --> [[gene.b0221|gene.b0221]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=fadE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0222|gene.b0222]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=gmhA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0443|gene.b0443]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0558|gene.b0558]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=ybcV; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0559|gene.b0559]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=ybcW; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1094|gene.b1094]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=acpP; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1675|gene.b1675]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=fumD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1702|gene.b1702]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=ppsA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1703|gene.b1703]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=ppsR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2344|gene.b2344]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3081|gene.b3081]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `is_component_of` --> [[complex.ecocyc.MONOMER-59|complex.ecocyc.MONOMER-59]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0081|gene.b0081]] `RegulonDB` `S` - regulator=PdhR; target=mraZ; function=-
- `represses` --> [[gene.b0082|gene.b0082]] `RegulonDB` `S` - regulator=PdhR; target=rsmH; function=-
- `represses` --> [[gene.b0083|gene.b0083]] `RegulonDB` `S` - regulator=PdhR; target=ftsL; function=-
- `represses` --> [[gene.b0084|gene.b0084]] `RegulonDB` `S` - regulator=PdhR; target=ftsI; function=-
- `represses` --> [[gene.b0085|gene.b0085]] `RegulonDB` `S` - regulator=PdhR; target=murE; function=-
- `represses` --> [[gene.b0086|gene.b0086]] `RegulonDB` `S` - regulator=PdhR; target=murF; function=-
- `represses` --> [[gene.b0087|gene.b0087]] `RegulonDB` `S` - regulator=PdhR; target=mraY; function=-
- `represses` --> [[gene.b0088|gene.b0088]] `RegulonDB` `S` - regulator=PdhR; target=murD; function=-
- `represses` --> [[gene.b0089|gene.b0089]] `RegulonDB` `S` - regulator=PdhR; target=ftsW; function=-
- `represses` --> [[gene.b0090|gene.b0090]] `RegulonDB` `S` - regulator=PdhR; target=murG; function=-
- `represses` --> [[gene.b0091|gene.b0091]] `RegulonDB` `S` - regulator=PdhR; target=murC; function=-
- `represses` --> [[gene.b0092|gene.b0092]] `RegulonDB` `S` - regulator=PdhR; target=ddlB; function=-
- `represses` --> [[gene.b0093|gene.b0093]] `RegulonDB` `S` - regulator=PdhR; target=ftsQ; function=-
- `represses` --> [[gene.b0094|gene.b0094]] `RegulonDB` `S` - regulator=PdhR; target=ftsA; function=-
- `represses` --> [[gene.b0095|gene.b0095]] `RegulonDB` `S` - regulator=PdhR; target=ftsZ; function=-
- `represses` --> [[gene.b0096|gene.b0096]] `RegulonDB` `S` - regulator=PdhR; target=lpxC; function=-
- `represses` --> [[gene.b0113|gene.b0113]] `RegulonDB` `C` - regulator=PdhR; target=pdhR; function=-
- `represses` --> [[gene.b0114|gene.b0114]] `RegulonDB` `C` - regulator=PdhR; target=aceE; function=-
- `represses` --> [[gene.b0115|gene.b0115]] `RegulonDB` `C` - regulator=PdhR; target=aceF; function=-
- `represses` --> [[gene.b0116|gene.b0116]] `RegulonDB` `C` - regulator=PdhR; target=lpd; function=-
- `represses` --> [[gene.b0428|gene.b0428]] `RegulonDB` `C` - regulator=PdhR; target=cyoE; function=-
- `represses` --> [[gene.b0429|gene.b0429]] `RegulonDB` `C` - regulator=PdhR; target=cyoD; function=-
- `represses` --> [[gene.b0430|gene.b0430]] `RegulonDB` `C` - regulator=PdhR; target=cyoC; function=-
- `represses` --> [[gene.b0431|gene.b0431]] `RegulonDB` `C` - regulator=PdhR; target=cyoB; function=-
- `represses` --> [[gene.b0432|gene.b0432]] `RegulonDB` `C` - regulator=PdhR; target=cyoA; function=-
- `represses` --> [[gene.b1109|gene.b1109]] `RegulonDB` `C` - regulator=PdhR; target=ndh; function=-
- `represses` --> [[gene.b2579|gene.b2579]] `RegulonDB` `S` - regulator=PdhR; target=grcA; function=-
- `represses` --> [[gene.b2975|gene.b2975]] `RegulonDB` `S` - regulator=PdhR; target=glcA; function=-
- `represses` --> [[gene.b2976|gene.b2976]] `RegulonDB` `S` - regulator=PdhR; target=glcB; function=-
- `represses` --> [[gene.b2977|gene.b2977]] `RegulonDB` `S` - regulator=PdhR; target=glcG; function=-
- `represses` --> [[gene.b2979|gene.b2979]] `RegulonDB` `S` - regulator=PdhR; target=glcD; function=-
- `represses` --> [[gene.b3603|gene.b3603]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=lldP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4467|gene.b4467]] `RegulonDB` `S` - regulator=PdhR; target=glcF; function=-
- `represses` --> [[gene.b4468|gene.b4468]] `RegulonDB` `S` - regulator=PdhR; target=glcE; function=-
- `represses` --> [[gene.b4810|gene.b4810]] `RegulonDB` `S` - regulator=PdhR; target=ftsO; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0113|gene.b0113]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACL9`
- `KEGG:ecj:JW0109;eco:b0113;ecoc:C3026_00470;`
- `GeneID:86862621;93777323;944827;`
- `GO:GO:0000987; GO:0003700; GO:0006355; GO:0045892; GO:0045893`

## Notes

Pyruvate dehydrogenase complex repressor
