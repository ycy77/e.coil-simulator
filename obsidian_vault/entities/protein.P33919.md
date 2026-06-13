---
entity_id: "protein.P33919"
entity_type: "protein"
name: "radD"
source_database: "UniProt"
source_id: "P33919"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "radD yejH yejI yejJ b2184 JW2172"
---

# radD

`protein.P33919`

## Static

- Type: `protein`
- Source: `UniProt:P33919`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Genetic interactions indicate that RecG or RadD are required for DNA repair in every replication cycle; they function in different pathways, each is essential in the absence of the other (PubMed:32644157). An accessory protein to RecA, it accelerates RecA-dependent DNA-strand exchange; this requires the ATPase activity of RadD (PubMed:35150260). Disassembles RecA filaments preformed on ssDNA (PubMed:35150260). In combination with RadA is important in repair of double-strand DNA breaks (DSB) (PubMed:25425430, PubMed:25484163). Has DNA-independent ATPase activity that is stimulated by single-stranded DNA-binding protein (SSB) (PubMed:27519413, PubMed:36614183). ATPase is stimulated by a peptide with the last 10 residues of SSB (PubMed:27519413, PubMed:36614183), but not when the SSB peptide's last Phe residue is missing (PubMed:27519413). Binds ssDNA; binding is slightly better in the presence of nucleotides (PubMed:27519413). May be involved in resolution of branched DNA intermediates that result from template switching in postreplication gaps. Binds to DNA structures with 3 branches that resemble replication forks (PubMed:31665437, PubMed:36614183). RadD contains helicase motifs, but no independent helicase activity has been observed (PubMed:31665437, PubMed:35150260) (Probable)...

## Biological Role

Catalyzes ATPASE-RXN (reaction.ecocyc.ATPASE-RXN).

## Annotation

FUNCTION: Genetic interactions indicate that RecG or RadD are required for DNA repair in every replication cycle; they function in different pathways, each is essential in the absence of the other (PubMed:32644157). An accessory protein to RecA, it accelerates RecA-dependent DNA-strand exchange; this requires the ATPase activity of RadD (PubMed:35150260). Disassembles RecA filaments preformed on ssDNA (PubMed:35150260). In combination with RadA is important in repair of double-strand DNA breaks (DSB) (PubMed:25425430, PubMed:25484163). Has DNA-independent ATPase activity that is stimulated by single-stranded DNA-binding protein (SSB) (PubMed:27519413, PubMed:36614183). ATPase is stimulated by a peptide with the last 10 residues of SSB (PubMed:27519413, PubMed:36614183), but not when the SSB peptide's last Phe residue is missing (PubMed:27519413). Binds ssDNA; binding is slightly better in the presence of nucleotides (PubMed:27519413). May be involved in resolution of branched DNA intermediates that result from template switching in postreplication gaps. Binds to DNA structures with 3 branches that resemble replication forks (PubMed:31665437, PubMed:36614183). RadD contains helicase motifs, but no independent helicase activity has been observed (PubMed:31665437, PubMed:35150260) (Probable). {ECO:0000269|PubMed:25425430, ECO:0000269|PubMed:25484163, ECO:0000269|PubMed:27519413, ECO:0000269|PubMed:31665437, ECO:0000269|PubMed:32644157, ECO:0000269|PubMed:35150260, ECO:0000269|PubMed:36614183, ECO:0000269|Ref.3, ECO:0000305|PubMed:25425430, ECO:0000305|PubMed:25484163, ECO:0000305|PubMed:27519413, ECO:0000305|PubMed:31665437, ECO:0000305|PubMed:35150260}.; FUNCTION: RadD and Uup are important in repair of stalled replication forks and postreplication gaps (PubMed:32644157). Lethal double radD-recG deletions are suppressed by a reduction in recA expression, by point mutations in priA helicase, and by deletions in recF, recO or uup, suggesting all these proteins create branched DNA intermediates requiring RadD or RecG for resolution (PubMed:32644157). {ECO:0000269|PubMed:32644157}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ATPASE-RXN|reaction.ecocyc.ATPASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2184|gene.b2184]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33919`
- `KEGG:ecj:JW2172;eco:b2184;ecoc:C3026_12215;`
- `GeneID:945529;`
- `GO:GO:0003677; GO:0003678; GO:0003697; GO:0005524; GO:0006301; GO:0006302; GO:0006412; GO:0008270; GO:0009410; GO:0010212; GO:0016887; GO:0051301`
- `EC:3.6.4.-`

## Notes

DNA repair protein RadD (EC 3.6.4.-) (Putative DNA repair helicase RadD)
