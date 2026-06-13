---
entity_id: "protein.P52076"
entity_type: "protein"
name: "qseB"
source_database: "UniProt"
source_id: "P52076"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "qseB ygiX b3025 JW2993"
---

# qseB

`protein.P52076`

## Static

- Type: `protein`
- Source: `UniProt:P52076`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of a two-component regulatory system QseB/QseC. Activates the flagella regulon by activating transcription of FlhDC. Currently it is not known whether this effect is direct or not. {ECO:0000269|PubMed:11929534}. QseB, "quorum-sensing E. coli regulator B", is the response regulator component of the QseB-QseC two-component system, which is one component of the quorum-sensing regulatory cascade involved in the regulation of biofilm formation, motility and flagella genes by activating transcription of flhDC, an operon that encodes the master regulator of these genes .QseB also regulates replication initiation by regulating DnaA expression . This protein also may have an undetermined role in metal metabolism, because qseBC deletion mutants show hypersensitivity to several toxic cations . QseB forms complexes with the chaperone DnaK and with the cell division protein FtsZ . QseB and QseC of enterohemorrhagic E. coli (EHEC) and of E. coli K-12 are almost identical; there are only three amino acid differences in QseB and only eight amino acid differences in QseC between these strains . It was demonstrated in EHEC that QseC directly senses and binds the bacterial hormone-like AI-3 signal and the host epineprhine/norepineprhine hormones, and it causes the autophosphorylation of QseC, which then transfers the phosphate group to QseB to activate it...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Member of a two-component regulatory system QseB/QseC. Activates the flagella regulon by activating transcription of FlhDC. Currently it is not known whether this effect is direct or not. {ECO:0000269|PubMed:11929534}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (3)

- `activates` --> [[gene.b3025|gene.b3025]] `RegulonDB` `S` - regulator=QseB; target=qseB; function=+
- `activates` --> [[gene.b3026|gene.b3026]] `RegulonDB` `S` - regulator=QseB; target=qseC; function=+
- `represses` --> [[gene.b3702|gene.b3702]] `RegulonDB|EcoCyc` `S` - regulator=QseB; target=dnaA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b3025|gene.b3025]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52076`
- `KEGG:ecj:JW2993;eco:b3025;ecoc:C3026_16525;`
- `GeneID:945369;`
- `GO:GO:0000156; GO:0000976; GO:0005829; GO:0006351; GO:0006355; GO:0010038; GO:0032993`

## Notes

Transcriptional regulatory protein QseB
