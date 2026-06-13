---
entity_id: "protein.P0ACJ5"
entity_type: "protein"
name: "decR"
source_database: "UniProt"
source_id: "P0ACJ5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "decR ybaO b0447 JW0437"
---

# decR

`protein.P0ACJ5`

## Static

- Type: `protein`
- Source: `UniProt:P0ACJ5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Plays a role in L-cysteine detoxification. Binds to the dlsT(yhaO)-yhaM operon promoter in the presence but not absence of L-cysteine; activates transcription from the dlsT(yhaO)-yhaM operon. No other DNA target was identified in strain K12 / BW25113. Thiosulfate does not activate its transcription function. Overexpression doubles hydrogen sulfide production in the presence of cysteine. {ECO:0000269|Ref.1}. DecR contains a helix-turn-helix motif to bind DNA in its N-terminal domain, and it appears to belong to the AsnC family of transcription factors (TFs) . DecR was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . DecR is a regulator with an important role in cysteine detoxification . The absence of decR increases the inhibitory effect on bacterial growth caused by cysteine . The presence of cysteine improves the interaction between DecR and the promoter region of the operon yhaOM, thereby causing activation . Compared to known global TFs, DecR exhibits some interesting regulatory features. First, it has more intragenic binding peaks and fewer peaks located within putative regulatory regions. Second, it has fewer binding peaks than global TFs, such as CRP, Lrp, Fnr, and ArcA. Third, it binds to more genes with putative functions...

## Annotation

FUNCTION: Plays a role in L-cysteine detoxification. Binds to the dlsT(yhaO)-yhaM operon promoter in the presence but not absence of L-cysteine; activates transcription from the dlsT(yhaO)-yhaM operon. No other DNA target was identified in strain K12 / BW25113. Thiosulfate does not activate its transcription function. Overexpression doubles hydrogen sulfide production in the presence of cysteine. {ECO:0000269|Ref.1}.

## Outgoing Edges (2)

- `activates` --> [[gene.b3110|gene.b3110]] `RegulonDB` `S` - regulator=DecR; target=cyuP; function=+
- `activates` --> [[gene.b4470|gene.b4470]] `RegulonDB` `S` - regulator=DecR; target=cyuA; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b0447|gene.b0447]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACJ5`
- `KEGG:ecj:JW0437;eco:b0447;ecoc:C3026_02190;`
- `GeneID:86862992;86945361;945091;`
- `GO:GO:0005829; GO:0009093; GO:0043200; GO:0043565; GO:2000144`

## Notes

DNA-binding transcriptional activator DecR
